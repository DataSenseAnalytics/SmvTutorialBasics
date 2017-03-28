from smv import *
from pyspark.sql.functions import *

from pyspark.sql.window import Window

__all__ = ['EmploymentByState']

class Employment(SmvCsvFile, SmvOutput):
    def path(self):
        return "input/employment/CB1200CZ11.csv"

    def failAtParsingError(self):
        return False



class EmploymentByState(SmvModule, SmvOutput):
    """Python ETL Example: employ by state"""

    def requiresDS(self):
        return [Employment]

    def run(self, i):
        df = i[Employment]
        return df.groupBy(col("ST")).agg(
                sum(col("EMP")).alias("EMP"),
                avg(col("PAYANN")/col("EMP")).alias("avg_PAYANN_per_EMP")  #add this line
                )

class PayEMPByState(SmvModule, SmvOutput):      #add a new module
    """Python ETL Example: average payroll per employee by state"""

    def requiresDS(self):
        return [Employment]  #still use the same input

    def run(self, i):
        df = i[Employment]
        return df.groupBy(col("ST")).agg(
          avg(col("PAYANN")/col("EMP")).alias("avg_PAYANN_per_EMP")
          )

# SMV Exercise 2
class EmploymentClean(SmvModule, SmvOutput):
    """Clean Employment Data"""

    def requiresDS(self):
        return [Employment]

    def run(self, i):
        df = i[Employment]
        return df.where(col("EMP_F").isNull()).smvSelectPlus(
                substring_index(substring_index(col("GEO_TTL"), ",", -1),")", 1).alias("ST_CD")
                ).where(length(col("ST_CD"))<3)

class EmpPayRollFeature(SmvModule, SmvOutput):
    """get overall, group averages and calculate differences in one step"""

    def requiresDS(self):
        return [EmploymentClean]

    def run(self, i):
        df = i[EmploymentClean]
        ctry_window = Window.partitionBy()
        state_window = Window.partitionBy("ST_CD")

        return df.smvSelectPlus((col("PAYANN")/col("EMP")).alias("PAYANN_per_EMP")).select(
                "ST",
                "ST_CD",
                "ZIPCODE",
                "PAYANN_per_EMP",
                (col("PAYANN_per_EMP") - avg(col("PAYANN_per_EMP")).over(ctry_window)).alias("diff_avg_ctry_PAYANN_per_EMP"),
                (col("PAYANN_per_EMP") - avg(col("PAYANN_per_EMP")).over(state_window)).alias("diff_avg_state_PAYANN_per_EMP")
                )

class EmpPayRollCounty(SmvModule, SmvOutput):
    """For each state, count counties with payroll per employee greater than state as well as country average"""

    def requiresDS(self):
        return [EmpPayRollFeature]

    def run(self, i):
        df = i[EmpPayRollFeature]

        return df.groupBy("ST_CD").agg(
                count("ST_CD").alias("cnt_counties"),
                sum(when((col("diff_avg_ctry_PAYANN_per_EMP")>0)&(col("diff_avg_state_PAYANN_per_EMP")>0),1).otherwise(0)).alias("cnt_counties_avg_ge_state_ctry")
                ).smvSelectPlus(
                (col("cnt_counties_avg_ge_state_ctry")/col("cnt_counties")*100).alias("pct_counties_avg_ge_state_ctry")
                ).orderBy(desc("pct_counties_avg_ge_state_ctry"))
