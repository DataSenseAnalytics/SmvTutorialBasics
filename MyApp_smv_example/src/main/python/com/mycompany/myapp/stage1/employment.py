from smv import *
from pyspark.sql.functions import col, sum, lit

from com.mycompany.myapp.stage1 import inputdata

__all__ = ['PythonEmploymentByState']

class PythonEmploymentByState(SmvPyModule):
    """Python ETL Example: employ by state"""

    def requiresDS(self):
        return [inputdata.PythonEmployment]

    def run(self, i):
        df = i[inputdata.PythonEmployment]
        return df.groupBy(col("ST")).agg(sum(col("EMP")).alias("EMP"))


class PythonEmploymentByStateCategory(SmvPyModule):
    """Python ETL Example: employment by state with category"""

    def requiresDS(self):
        return [PythonEmploymentByState]

    def run(self, i):
        df = i[PythonEmploymentByState]
        return df.smvSelectPlus((col("EMP") > lit(1000000)).alias("cat_high_emp"))
