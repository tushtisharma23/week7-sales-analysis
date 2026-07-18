import pandas as pd


class DataCleaner:

    def __init__(self, data):
        self.data = data

    def clean_data(self):
        """Clean and preprocess the sales dataset."""

        if self.data is None:
            print("No data available for cleaning.")
            return None

        print("\n===== DATA CLEANING =====")

        # Remove duplicate records
        duplicate_count = self.data.duplicated().sum()
        self.data = self.data.drop_duplicates()

        print(f"Duplicate records removed: {duplicate_count}")

        # Convert order date to datetime
        if "order_date" in self.data.columns:
            self.data["order_date"] = pd.to_datetime(
                self.data["order_date"],
                errors="coerce"
            )

        # Handle missing numerical values
        numerical_columns = self.data.select_dtypes(
            include="number"
        ).columns

        for column in numerical_columns:
            if self.data[column].isnull().any():
                self.data[column] = self.data[column].fillna(
                    self.data[column].median()
                )

        # Handle missing text values
        text_columns = self.data.select_dtypes(
            include="object"
        ).columns

        for column in text_columns:
            if self.data[column].isnull().any():
                self.data[column] = self.data[column].fillna(
                    "Unknown"
                )

        print(f"Missing values remaining: {self.data.isnull().sum().sum()}")
        print("Data cleaning completed successfully!")

        return self.data

    def save_cleaned_data(
        self,
        output_path="data/processed/cleaned_sales_data.csv"
    ):
        """Save the cleaned dataset to a CSV file."""

        if self.data is None:
            print("No cleaned data available to save.")
            return

        self.data.to_csv(output_path, index=False)

        print(f"Cleaned data saved to: {output_path}")