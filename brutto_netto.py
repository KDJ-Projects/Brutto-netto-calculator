import tkinter as tk
from tkinter import ttk
from tkinter.constants import NUMERIC

window = tk.Tk()
window.title("Bruto - Netto bereking")
window.geometry("+1615+400")

def brutto_netto_calc():
   
    try:

        gross_monthly_salary = int(gross_monthly_salary_amount_entry.get())

        days_worked = int(days_worked_amount_entry.get())

        # Fees only for worked day!
        daily_meal_fee = int(daily_meal_fee_amount_entry.get())

        daily_road_fee = int(daily_road_fee_amount_entry.get())

        # Monthly fees (Carwash, costs reimbursement and mobile phone subscription)
        monthly_carwash_GSM_expences_fee = int(monthly_carwash_GSM_expences_fee_amount_entry.get())

        total_daily_meal_fee = days_worked * daily_meal_fee
        total_daily_road_fee = days_worked * daily_road_fee

    except Exception:
            error = tk.Toplevel(window)
            error.title("Error")
            error.geometry("+1700+430")

            error_warning_lbl = ttk.Label(error, text="Geef waardes in!", foreground="red")
            error_warning_lbl.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 5))

            quit_btn = ttk.Button(error, text="Sluit", command=error.destroy)
            quit_btn.grid(row=1, column=0, columnspan=2, padx=(10, 10), pady=(0, 10))

    # Calculation for monthly RSZ
    rsz_percentage = 0.1307
    rsz_month_amount = float(gross_monthly_salary_amount_entry.get()) * rsz_percentage

    # Calculation for addiditonal monthly special RSZ contribution => Belgium
    # € 55,80 EUR + 1,1% van het deel > € 6.570,54
    quarter_min_amount = 55.80
    quarter_percentage = 1.1 / 100
    quarter_share = 6570.54
    quarter_gross_salary = gross_monthly_salary * 3

    calc_quarter_rest_amount = (quarter_gross_salary - quarter_share)
    rsz_special_contribution = round(((calc_quarter_rest_amount * quarter_percentage) + quarter_min_amount) / 3, 2)

    # Calculation for total monthly net fees
    net_total_fees = total_daily_meal_fee + total_daily_road_fee + monthly_carwash_GSM_expences_fee

    # Calculation for net monthly salary
    net_taxable_wages = (gross_monthly_salary - rsz_month_amount)
    monthly_witholding_tax = 36.811227424364431 / 100
    tax_monthly_amount = net_taxable_wages * monthly_witholding_tax
    net_monthly_wages = net_taxable_wages - tax_monthly_amount - rsz_special_contribution

    # Calculating yearly tax rate
    gross_year_wages = gross_monthly_salary * 12
    net_year_wages = net_monthly_wages * 12
    rest_year_wages = gross_year_wages - net_year_wages
    yearly_tax_percentage = (rest_year_wages/ gross_year_wages) * 100

    # Popup window for amounts
    popup = tk.Toplevel(window)
    popup.title("Loon en vergoedingen")
    popup.geometry("+1612+700")

    ## LABELS POPUP ##
    gross_month_description_lbl = ttk.Label(popup, text="Bruto maand verloning:")
    gross_month_description_lbl.grid(row=1, column=0, sticky="W", padx=(10, 10), pady=(10, 10))
    gross_month_wages_lbl = ttk.Label(popup, text=f"{gross_monthly_salary} €")
    gross_month_wages_lbl.grid(row=1, column=1, sticky="E", padx=(0, 10), pady=(10, 10))

    rsz_description_lbl = ttk.Label(popup, text=f"RSZ maand bedrag ({rsz_percentage * 100}%):")
    rsz_description_lbl.grid(row=2, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    rsz_procent_lbl = ttk.Label(popup, text=f"{rsz_month_amount} €")
    rsz_procent_lbl.grid(row=2, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    rsz_special_net_contribution_description_lbl = ttk.Label(popup, text="Bijzondere rsz bijdrag:")
    rsz_special_net_contribution_description_lbl.grid(row=3, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    rsz_special_net_contribution_amount_lbl = ttk.Label(popup, text=f"{rsz_special_contribution} €")
    rsz_special_net_contribution_amount_lbl.grid(row=3, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    tax_monthly_description_lbl = ttk.Label(popup, text=f"Bedrijfsvoorheffing ({round(monthly_witholding_tax * 100, 2)}%):")
    tax_monthly_description_lbl.grid(row=4, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    tax_monthly_amount_lbl = ttk.Label(popup,text=f"{round(tax_monthly_amount, 2)} €")
    tax_monthly_amount_lbl.grid(row=4, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    net_fees_description_lbl = ttk.Label(popup, text=f"Netto vergoedingen ({days_worked} dagen):")
    net_fees_description_lbl.grid(row=5, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    net_fees_amount_lbl = ttk.Label(popup, text=f"{net_total_fees} €")
    net_fees_amount_lbl.grid(row=5, column=1, sticky="E", padx=(0, 10), pady=(0,10))

    net_monthly_wages_description_lbl = ttk.Label(popup, text="Netto maand loon:")
    net_monthly_wages_description_lbl.grid(row=6, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    net_monthly_wages_lbl = ttk.Label(popup, text=f"{round(net_monthly_wages, 2)} €")
    net_monthly_wages_lbl.grid(row=6, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    net_monthly_wages_and_fee_description_lbl = ttk.Label(popup, text="Netto loon + vergoedingen:")
    net_monthly_wages_and_fee_description_lbl.grid(row=7, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    net_monthly_wages_and_fee_amount_lbl = ttk.Label(popup, text=f"{round(net_monthly_wages + net_total_fees, 2)} €")
    net_monthly_wages_and_fee_amount_lbl.grid(row=7, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    separator_lbl = ttk.Label(popup, text="---------------------------------------")
    separator_lbl.grid(row=8, column=0, columnspan=3)

    gross_year_wages_description_lbl = ttk.Label(popup, text="Brutto jaarverloning:")
    gross_year_wages_description_lbl.grid(row=9, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    gross_year_wages_amount_lbl = ttk.Label(popup, text=f"{round(gross_year_wages, 2)} €")
    gross_year_wages_amount_lbl.grid(row=9, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    net_yearly_wages_description_lbl = ttk.Label(popup, text="Netto jaarverloning:")
    net_yearly_wages_description_lbl.grid(row=10, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    net_yearly_wages_amount_lbl = ttk.Label(popup, text=f"{round(net_monthly_wages * 12, 2)} €")
    net_yearly_wages_amount_lbl.grid(row=10, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

    yearly_tax_amount_description_lbl = ttk.Label(popup, text=f"Jaarlijks belasting ({round(yearly_tax_percentage, 2)}%):")
    yearly_tax_amount_description_lbl.grid(row=12, column=0, sticky="W", padx=(10, 10), pady=(0, 10))
    yearly_tax_amount_lbl = ttk.Label(popup, text=f"{round(gross_year_wages - (net_monthly_wages * 12), 2)} €")
    yearly_tax_amount_lbl.grid(row=12, column=1, sticky="E", padx=(0, 10), pady=(0, 10))

## LABELS & ENTRYS MAIN ##
gross_monthly_salary_description_lbl = ttk.Label(window, text="Bruto maand verloning:")
gross_monthly_salary_description_lbl.grid(row=0, column=0, sticky="W", padx=(20, 0), pady=(5, 0))
gross_monthly_salary_amount_entry = ttk.Entry(window, width=5)
gross_monthly_salary_amount_entry.grid(row=0, column=1, sticky="E", padx=(0, 20), pady=(10, 0))
gross_monthly_salary_amount_entry.focus()

days_worked_description_lbl = ttk.Label(window, text="Aantal gewerkte dagen:")
days_worked_description_lbl.grid(row=1, column=0, sticky="W", padx=(20, 0), pady=(5, 0))
days_worked_amount_entry = ttk.Entry(window, width=5)
days_worked_amount_entry.grid(row=1, column=1, sticky="E", padx=(0, 20), pady=(10, 0))

daily_meal_fee_description_lbl = ttk.Label(window, text="Maaltijd vergoeding bedrag:")
daily_meal_fee_description_lbl.grid(row=2, column=0, sticky="W", padx=(20, 0), pady=(5, 0))
daily_meal_fee_amount_entry = ttk.Entry(window, width=5)
daily_meal_fee_amount_entry.grid(row=2, column=1, sticky="E", padx=(0, 20), pady=(10, 0))

daily_road_fee_description_lbl = ttk.Label(window, text="Baan vergoeding bedrag:")
daily_road_fee_description_lbl.grid(row=3, column=0, sticky="W", padx=(20, 0), pady=(5, 0))
daily_road_fee_amount_entry = ttk.Entry(window, width=5)
daily_road_fee_amount_entry.grid(row=3, column=1, sticky="E", padx=(0, 20), pady=(10, 0))

monthly_carwash_GSM_expences_fee_description_lbl = ttk.Label(window, text="Vergoeding maand bedrag:")
monthly_carwash_GSM_expences_fee_description_lbl.grid(row=4, column=0, sticky="W", padx=(20, 0), pady=(5, 0))
monthly_carwash_GSM_expences_fee_amount_entry = ttk.Entry(window, width=5)
monthly_carwash_GSM_expences_fee_amount_entry.grid(row=4, column=1, sticky="E", padx=(0, 20), pady=(10, 0))

## BUTTONS MAIN ##
calculate_btn = ttk.Button(window,text="Bereken", command=brutto_netto_calc)
calculate_btn.grid(row=5, column=0, padx=(0, 0), pady=(10, 10))

quit_btn = ttk.Button(window, text="Sluit", command=window.destroy)
quit_btn.grid(row=5, column=1, padx=(0, 30), pady=(10, 10))

window.mainloop()
