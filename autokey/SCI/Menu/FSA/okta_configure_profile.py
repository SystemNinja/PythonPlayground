cost_center = ["FSA-Academic Instruction","FSA-Facilities Management","FSA-Regulatory Operations","FSA-Program Management","FSA-Marketing","FSA-Business Development","FSA-Finance","FSA-Student Advisory","FSA-Admissions","FSA-Career Success","FSA-People & Talent","FSA-Executive","FSA-Engineering & IT","FSA-Product Development", ""]
manager_level = ["Individual Contributor", "Director", "Sr. Director", "Manager", "Supervisor", "Vice President", "Subsidiary Senior Management", "Assoc Director", "Sr. Manager", ""]
pay_basis = ["Hourly", "Salary"]
employee_type = ["Regular", "Cohort Instruction & Support", "Fellow"]
exemption_status = ["Exempt", "Non-exempt"]
time_type = ["Part time", "Full time"]

select_cost_center = dialog.list_menu(cost_center, "Select cost center")
select_manager_level = dialog.list_menu(manager_level, "Select manager level")
select_employee_type = dialog.list_menu(employee_type, "Select employee type")
select_exemption_status = dialog.list_menu(exemption_status, "Select exemption status")
select_time_type = dialog.list_menu(time_type, "Select time type")

keyboard.send_keys(select_cost_center.data)
keyboard.send_key("<tab>")
keyboard.send_keys("Fullstack Academy")
keyboard.send_key("<tab>", 4)
keyboard.send_keys(select_manager_level.data)
keyboard.send_key("<tab>")
if(select_time_type.data == "Full time"):
    keyboard.send_keys(pay_basis[1])
    keyboard.send_key("<tab>")
else:
    keyboard.send_keys(pay_basis[0])
    keyboard.send_key("<tab>")
keyboard.send_keys(select_exemption_status.data)
keyboard.send_key("<tab>")
keyboard.send_keys(select_employee_type.data)
keyboard.send_key("<tab>",2)
keyboard.send_keys(select_time_type.data)