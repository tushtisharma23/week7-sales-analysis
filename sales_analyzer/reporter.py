import os
import pandas as pd


class SalesReporter:

    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.output_dir = "data/reports"

        os.makedirs(self.output_dir, exist_ok=True)

    def generate_summary_report(self):
        """Display and save a summary of the sales analysis."""

        stats = self.analyzer.calculate_basic_stats()
        peak_data = self.analyzer.peak_sales_month()

        if stats is None:
            print("No data available for report.")
            return

        report = []

        report.append("SALES DATA ANALYSIS REPORT")
        report.append("=" * 40)

        report.append("\nBASIC STATISTICS")
        report.append("-" * 40)
        report.append(
            f"Total Sales: Rs. {stats['total_sales']:,.2f}"
        )
        report.append(
            f"Total Orders: {stats['total_orders']}"
        )
        report.append(
            f"Average Order Value: Rs. "
            f"{stats['average_order_value']:,.2f}"
        )
        report.append(
            f"Unique Customers: {stats['unique_customers']}"
        )
        report.append(
            f"Unique Products: {stats['unique_products']}"
        )

        if peak_data:
            peak_month, peak_sales = peak_data

            report.append("\nPEAK SALES PERIOD")
            report.append("-" * 40)
            report.append(
                f"Highest Sales Month: {peak_month}"
            )
            report.append(
                f"Sales: Rs. {peak_sales:,.2f}"
            )

        report_text = "\n".join(report)

        print("\n" + report_text)

        file_path = f"{self.output_dir}/sales_summary.txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(report_text)

        print(f"\nSummary report saved to: {file_path}")

    def export_to_csv(self):
        """Export analysis results to CSV files."""

        category_data = self.analyzer.sales_by_category()
        monthly_data = self.analyzer.monthly_sales_trends()
        customer_data = self.analyzer.customer_analysis()
        region_data = self.analyzer.sales_by_region()

        category_data.to_csv(
            f"{self.output_dir}/category_analysis.csv"
        )

        monthly_data.to_csv(
            f"{self.output_dir}/monthly_analysis.csv"
        )

        customer_data.to_csv(
            f"{self.output_dir}/customer_analysis.csv"
        )

        region_data.to_csv(
            f"{self.output_dir}/regional_analysis.csv"
        )

        print("\nCSV reports exported successfully!")

    def export_to_excel(self):
        """Export complete analysis to an Excel workbook."""

        file_path = f"{self.output_dir}/sales_analysis_report.xlsx"

        with pd.ExcelWriter(
            file_path,
            engine="openpyxl"
        ) as writer:

            stats = self.analyzer.calculate_basic_stats()

            pd.DataFrame(
                [stats]
            ).to_excel(
                writer,
                sheet_name="Summary",
                index=False
            )

            self.analyzer.sales_by_category().to_excel(
                writer,
                sheet_name="Category Analysis"
            )

            self.analyzer.top_products().to_excel(
                writer,
                sheet_name="Top Products"
            )

            self.analyzer.monthly_sales_trends().to_excel(
                writer,
                sheet_name="Monthly Trends"
            )

            self.analyzer.customer_analysis().to_excel(
                writer,
                sheet_name="Customer Analysis"
            )

            self.analyzer.sales_by_region().to_excel(
                writer,
                sheet_name="Regional Analysis"
            )

        print(f"\nExcel report generated: {file_path}")

    def generate_all_reports(self):
        """Generate all available reports."""

        print("\n===== GENERATING REPORTS =====")

        self.generate_summary_report()
        self.export_to_csv()
        self.export_to_excel()

        print("\nAll reports generated successfully!")