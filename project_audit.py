import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import urllib.parse

# --- 1. SETUP CONNECTION (The Modern Way) ---
print("[INFO] Configuring Connection...")

# We build the connection URL safely
server = r"Krithi-PC\SQLEXPRESS"
database = "EnterpriseDW"
driver = "ODBC Driver 17 for SQL Server" 
# NOTE: If "ODBC Driver 17..." fails, change it back to just "SQL Server"

# Create the connection string
connection_string = (
    f"mssql+pyodbc://@{server}/{database}?"
    f"driver={driver}&trusted_connection=yes"
)

try:
    # Create the SQL Engine
    engine = create_engine(connection_string)
    print(f"[SUCCESS] Engine created for {server}")

    # --- 2. EXTRACT DATA ---
    query = "SELECT * FROM vw_Enterprise_Analytics"
    print("[INFO] Loading data (This may take 10 seconds)...")
    
    # Pandas reads from the 'engine' now (No Warnings!)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    
    print(f"[SUCCESS] Data Loaded: {len(df)} rows found.")

    # --- 3. ANALYTICS REPORT ---
    print("\n" + "="*30)
    print("EXECUTIVE DATA REPORT")
    print("="*30)
    
    # Check A: Total Revenue
    total_rev = df['TotalRevenueUSD'].sum()
    print(f"Total Enterprise Revenue: ${total_rev:,.2f}")

    # Check B: Top 5 Brands
    top_brands = df.groupby('Brand')['TotalRevenueUSD'].sum().sort_values(ascending=False).head(5)
    print("\nTop 5 Brands by Revenue:")
    print(top_brands)

    # --- 4. VISUALIZE ---
    print("\n[INFO] Generating Bar Chart...")
    
    plt.figure(figsize=(10, 6))
    top_brands.plot(kind='bar', color='royalblue')
    
    plt.title('Top 5 Brands by Revenue (USD)')
    plt.xlabel('Brand Name')
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    print("[SUCCESS] Dashboard generated. Check the popup window.")
    plt.show()

except Exception as e:
    print("\n[ERROR] Connection Failed.")
    print(f"Error Detail: {e}")
    print("\nTROUBLESHOOTING:")
    print("1. Ensure you ran 'pip install sqlalchemy'.")
    print("2. Try changing the 'driver' variable in the code to 'SQL Server'.")