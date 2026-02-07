from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, sum as _sum
import os

# 1. Start Spark Engine (Quiet Mode)
spark = SparkSession.builder \
    .appName("Enterprise_BigData") \
    .master("local[*]") \
    .config("spark.ui.showConsoleProgress", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR") # Hides the messy warnings
print("[INFO] Spark Engine Online")

# 2. Load Data 
# NOTE: Make sure these files are in the SAME folder as this script!
print("[INFO] Loading CSV Data...")

try:
    # Check if files exist first to avoid long error messages
    if not os.path.exists("Sales.csv") or not os.path.exists("Products.csv"):
        print("[ERROR] Cannot find 'Sales.csv' or 'Products.csv'.")
        print("        Please make sure they are in this folder:")
        print(f"        {os.getcwd()}")
        spark.stop()
        exit()

    df_sales = spark.read.csv("Sales.csv", header=True, inferSchema=True)
    df_products = spark.read.csv("Products.csv", header=True, inferSchema=True)

    # 3. Transform & Join
    print("[INFO] Joining Sales and Products...")
    df_products = df_products.withColumnRenamed("ProductKey", "ProdKey")
    
    # Inner Join
    df_joined = df_sales.join(df_products, df_sales.ProductKey == df_products.ProdKey, "inner")

    # 4. Aggregate
    print("[INFO] Calculating High-Volume Categories...")
    top_cats = df_joined.groupBy("Category") \
        .agg(_sum("Quantity").alias("Total_Volume")) \
        .orderBy(desc("Total_Volume"))

    # Show the Table
    print("\n--- RESULTS ---")
    top_cats.show()

except Exception as e:
    print(f"[ERROR] {e}")

finally:
    spark.stop()
    print("[INFO] Spark Session Stopped")