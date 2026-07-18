import os
import matplotlib.pyplot as plt


class SalesVisualizer:

    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.output_dir = "data/reports"

        os.makedirs(self.output_dir, exist_ok=True)

    def create_monthly_sales_chart(self):
        """Create a line chart showing monthly sales trends."""

        monthly_data = self.analyzer.monthly_sales_trends()

        plt.figure(figsize=(10, 6))

        plt.plot(
            monthly_data.index.astype(str),
            monthly_data["total_sales"],
            marker="o"
        )

        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        file_path = f"{self.output_dir}/monthly_sales_trend.png"
        plt.savefig(file_path)
        plt.close()

        print(f"Monthly sales chart saved to: {file_path}")

    def create_category_bar_chart(self):
        """Create a bar chart showing sales by category."""

        category_data = self.analyzer.sales_by_category()

        plt.figure(figsize=(10, 6))

        category_data.plot(kind="bar")

        plt.title("Sales by Product Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()

        file_path = f"{self.output_dir}/category_sales.png"
        plt.savefig(file_path)
        plt.close()

        print(f"Category sales chart saved to: {file_path}")

    def create_category_pie_chart(self):
        """Create a pie chart showing category sales distribution."""

        category_data = self.analyzer.sales_by_category()

        plt.figure(figsize=(8, 8))

        category_data.plot(
            kind="pie",
            autopct="%1.1f%%"
        )

        plt.title("Sales Distribution by Category")
        plt.ylabel("")
        plt.tight_layout()

        file_path = f"{self.output_dir}/category_sales_pie.png"
        plt.savefig(file_path)
        plt.close()

        print(f"Category pie chart saved to: {file_path}")

    def create_region_chart(self):
        """Create a bar chart showing sales by region."""

        region_data = self.analyzer.sales_by_region()

        plt.figure(figsize=(8, 6))

        region_data.plot(kind="bar")

        plt.title("Sales by Region")
        plt.xlabel("Region")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=0)
        plt.tight_layout()

        file_path = f"{self.output_dir}/regional_sales.png"
        plt.savefig(file_path)
        plt.close()

        print(f"Regional sales chart saved to: {file_path}")

    def create_all_visualizations(self):
        """Generate all sales visualizations."""

        print("\n===== GENERATING VISUALIZATIONS =====")

        self.create_monthly_sales_chart()
        self.create_category_bar_chart()
        self.create_category_pie_chart()
        self.create_region_chart()

        print("\nAll visualizations generated successfully!")