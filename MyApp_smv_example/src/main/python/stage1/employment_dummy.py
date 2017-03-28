from smv import *
from pyspark.sql.functions import *

__all__ = ['EstabByState']

class EmploymentDummy(SmvCsvFile):
    def path(self):
        return "input/employment_dummy/CB1200CZ11_dummy.csv"

    def dqm(self):
        """An example DQM policy"""
        return SmvDQM().add(FailParserCountPolicy(10))



class EstabByState(SmvModule, SmvOutput):
    """Python ETL Example: establishments by state"""

    def requiresDS(self):
        return [EmploymentDummy]

    def run(self, i):
        df = i[EmploymentDummy]
        return df.groupBy(col("ST")).agg(
                sum(col("ESTAB")).alias("sum_ESTAB")
                )
