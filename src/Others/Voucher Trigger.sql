-- TRIGGER FOR VOUCHER TRACKING

DELIMITER //
DROP TRIGGER IF EXISTS after_items_voucher_insert//
CREATE TRIGGER after_items_voucher_insert AFTER INSERT ON items_voucher FOR EACH ROW
BEGIN
INSERT INTO items_voucheraudit(id, voucher_number, payee_name, BE, document_number, amount, request_number, 
			received_from_BE_by_cage1, received_from_BE_by_cage1_user, date_received_from_BE_by_cage1, 
            for_head_of_section, voucher_and_cheque_received_by_BE, voucher_and_cheque_received_by, 
            date_voucher_and_cheque_received_by_BE, received_from_BE_by_cage1_2nd_time, 
            received_from_BE_by_cage1_2nd_time_user, date_received_from_BE_by_cage1_2nd_time, 
            received_at_salary_unit, received_at_salary_unit_user, date_received_at_salary_unit, 
            voucher_generated, voucher_generated_user, payment_method, date_generated, 
            received_by_bank_transfer, received_by_bank_transfer_user, third_party, 
            date_received_by_bank_transfer, received_by_CPO, received_by_CPO_user, payment_type, 
            date_received_by_CPO, received_from_CPO_by_cage1, received_from_CPO_by_cage1_user, 
            date_received_from_CPO_by_cage1, received_from_CPO_by_cage2, received_from_CPO_by_cage2_user, 
            date_received_from_CPO_by_cage2, received_by_store, received_by_store_user, date_received_by_store, 
            hold_voucher, date_hold, voucher_returned_to_BE, voucher_returned_to_BE_user, date_returned, 
            collected_by, received_by_accounting_unit, received_by_accounting_unit_user, 
            date_received_by_accounting_unit, received_by_revenue, received_by_revenue_user, 
            date_received_by_revenue, location, timestamp, last_updated, comments) 
            
            VALUES(new.id, new.voucher_number, new.payee_name, new.BE, new.document_number, new.amount, new.request_number, 
			new.received_from_BE_by_cage1, new.received_from_BE_by_cage1_user, new.date_received_from_BE_by_cage1, 
            new.for_head_of_section, new.voucher_and_cheque_received_by_BE, new.voucher_and_cheque_received_by, 
            new.date_voucher_and_cheque_received_by_BE, new.received_from_BE_by_cage1_2nd_time, 
            new.received_from_BE_by_cage1_2nd_time_user, new.date_received_from_BE_by_cage1_2nd_time, 
            new.received_at_salary_unit, new.received_at_salary_unit_user, new.date_received_at_salary_unit, 
            new.voucher_generated, new.voucher_generated_user, new.payment_method, new.date_generated, 
            new.received_by_bank_transfer, new.received_by_bank_transfer_user, new.third_party, 
            new.date_received_by_bank_transfer, new.received_by_CPO, new.received_by_CPO_user, new.payment_type, 
            new.date_received_by_CPO, new.received_from_CPO_by_cage1, new.received_from_CPO_by_cage1_user, 
            new.date_received_from_CPO_by_cage1, new.received_from_CPO_by_cage2, new.received_from_CPO_by_cage2_user, 
            new.date_received_from_CPO_by_cage2, new.received_by_store, new.received_by_store_user, new.date_received_by_store, 
            new.hold_voucher, new.date_hold, new.voucher_returned_to_BE, new.voucher_returned_to_BE_user, new.date_returned, 
            new.collected_by, new.received_by_accounting_unit, new.received_by_accounting_unit_user, 
            new.date_received_by_accounting_unit, new.received_by_revenue, new.received_by_revenue_user, 
            new.date_received_by_revenue, new.location, new.timestamp, new.last_updated, new.comments);
END//
DELIMITER ;



DELIMITER //
DROP TRIGGER IF EXISTS after_items_voucher_update//
CREATE TRIGGER after_items_voucher_update AFTER UPDATE ON items_voucher FOR EACH ROW
BEGIN
	INSERT INTO items_voucheraudit(id, voucher_number, payee_name, BE, document_number, amount, request_number, 
		received_from_BE_by_cage1, received_from_BE_by_cage1_user, date_received_from_BE_by_cage1, 
		for_head_of_section, voucher_and_cheque_received_by_BE, voucher_and_cheque_received_by, 
		date_voucher_and_cheque_received_by_BE, received_from_BE_by_cage1_2nd_time, 
		received_from_BE_by_cage1_2nd_time_user, date_received_from_BE_by_cage1_2nd_time, 
		received_at_salary_unit, received_at_salary_unit_user, date_received_at_salary_unit, 
		voucher_generated, voucher_generated_user, payment_method, date_generated, 
		received_by_bank_transfer, received_by_bank_transfer_user, third_party, 
		date_received_by_bank_transfer, received_by_CPO, received_by_CPO_user, payment_type, 
		date_received_by_CPO, received_from_CPO_by_cage1, received_from_CPO_by_cage1_user, 
		date_received_from_CPO_by_cage1, received_from_CPO_by_cage2, received_from_CPO_by_cage2_user, 
		date_received_from_CPO_by_cage2, received_by_store, received_by_store_user, date_received_by_store, 
		hold_voucher, date_hold, voucher_returned_to_BE, voucher_returned_to_BE_user, date_returned, 
		collected_by, received_by_accounting_unit, received_by_accounting_unit_user, 
		date_received_by_accounting_unit, received_by_revenue, received_by_revenue_user, 
		date_received_by_revenue, location, timestamp, last_updated, comments) 
		
	VALUES(new.id, new.voucher_number, new.payee_name, new.BE, new.document_number, new.amount, new.request_number, 
		new.received_from_BE_by_cage1, new.received_from_BE_by_cage1_user, new.date_received_from_BE_by_cage1, 
		new.for_head_of_section, new.voucher_and_cheque_received_by_BE, new.voucher_and_cheque_received_by, 
		new.date_voucher_and_cheque_received_by_BE, new.received_from_BE_by_cage1_2nd_time, 
		new.received_from_BE_by_cage1_2nd_time_user, new.date_received_from_BE_by_cage1_2nd_time, 
		new.received_at_salary_unit, new.received_at_salary_unit_user, new.date_received_at_salary_unit, 
		new.voucher_generated, new.voucher_generated_user, new.payment_method, new.date_generated, 
		new.received_by_bank_transfer, new.received_by_bank_transfer_user, new.third_party, 
		new.date_received_by_bank_transfer, new.received_by_CPO, new.received_by_CPO_user, new.payment_type, 
		new.date_received_by_CPO, new.received_from_CPO_by_cage1, new.received_from_CPO_by_cage1_user, 
		new.date_received_from_CPO_by_cage1, new.received_from_CPO_by_cage2, new.received_from_CPO_by_cage2_user, 
		new.date_received_from_CPO_by_cage2, new.received_by_store, new.received_by_store_user, new.date_received_by_store, 
		new.hold_voucher, new.date_hold, new.voucher_returned_to_BE, new.voucher_returned_to_BE_user, new.date_returned, 
		new.collected_by, new.received_by_accounting_unit, new.received_by_accounting_unit_user, 
		new.date_received_by_accounting_unit, new.received_by_revenue, new.received_by_revenue_user, 
		new.date_received_by_revenue, new.location, new.timestamp, new.last_updated, new.comments);

END//
DELIMITER ;












-- GRATUITY PAYMENT TRIGGER


DELIMITER //
DROP TRIGGER IF EXISTS after_items_gratuitypayment_insert//
CREATE TRIGGER after_items_gratuitypayment_insert AFTER INSERT ON items_gratuitypayment FOR EACH ROW
BEGIN
	INSERT INTO items_gratuitypaymentaudit(id, employment_number, name, received_from_records, date_received_from_records, 
		approved_and_sumitted_to_NAO, date_sumitted_to_NAO, 
		received_from_NAO, date_received_from_NAO, approved_by_NAO_and_sumitted_to_PMO, 
		date_sumitted_to_PMO, disapproved_by_AGD_and_returned_to_ministry_or_department,
		disapproved_by_NAO_and_returned_to_ministry_or_department, date_returned_to_ministry_or_department, 
		position_last_held, ministry_or_department, 
		date_of_birth, date_of_retirement, voucher_number, 
		gratuity_amount, pension_p_a_amount, pension_p_m_amount, one_by_six_deduction, 
		salary_deduction, other_deduction, 
		total_deduction, date_paid, net_gratuity, add_additional_gratuity, 
		second_position_last_held, second_ministry_or_department, 
		second_date_of_retirement, second_voucher_number, second_gratuity_amount, second_pension_p_a_amount, 
		second_pension_p_m_amount, second_one_by_six_deduction, second_salary_deduction, second_other_deduction, 
		second_total_deduction, second_date_paid, second_net_gratuity, retirement_comments, 
		gratuity_comments, start_date, end_date, timestamp, added_by, last_updated, last_updated_by, comments) 


	VALUES(new.id, new.employment_number, name, new.received_from_records, new.date_received_from_records, 
		new.approved_and_sumitted_to_NAO, new.date_sumitted_to_NAO, 
		new.received_from_NAO, new.date_received_from_NAO, new.approved_by_NAO_and_sumitted_to_PMO, 
		new.date_sumitted_to_PMO, new.disapproved_by_AGD_and_returned_to_ministry_or_department,
		new.disapproved_by_NAO_and_returned_to_ministry_or_department, new.date_returned_to_ministry_or_department, 
		new.position_last_held, new.ministry_or_department, 
		new.date_of_birth, new.date_of_retirement, new.voucher_number, 
		new.gratuity_amount, new.pension_p_a_amount, new.pension_p_m_amount, new.one_by_six_deduction, 
		new.salary_deduction, new.other_deduction, 
		new.total_deduction, new.date_paid, new.net_gratuity, new.add_additional_gratuity, 
		new.second_position_last_held, new.second_ministry_or_department, 
		new.second_date_of_retirement, new.second_voucher_number, new.second_gratuity_amount, new.second_pension_p_a_amount, 
		new.second_pension_p_m_amount, new.second_one_by_six_deduction, new.second_salary_deduction, new.second_other_deduction, 
		new.second_total_deduction, new.second_date_paid, new.second_net_gratuity, new.retirement_comments, 
		new.gratuity_comments, new.start_date, new.end_date, new.timestamp, new.added_by, new.last_updated, new.last_updated_by, new.comments);
END//
DELIMITER ;



DELIMITER //
DROP TRIGGER IF EXISTS after_items_gratuitypayment_update//
CREATE TRIGGER after_items_gratuitypayment_update AFTER UPDATE ON items_gratuitypayment FOR EACH ROW
BEGIN
	INSERT INTO items_gratuitypaymentaudit(id, employment_number, name, received_from_records, date_received_from_records, 
		approved_and_sumitted_to_NAO, date_sumitted_to_NAO, 
		received_from_NAO, date_received_from_NAO, approved_by_NAO_and_sumitted_to_PMO, 
		date_sumitted_to_PMO, disapproved_by_AGD_and_returned_to_ministry_or_department,
		disapproved_by_NAO_and_returned_to_ministry_or_department, date_returned_to_ministry_or_department, 
		position_last_held, ministry_or_department, 
		date_of_birth, date_of_retirement, voucher_number, 
		gratuity_amount, pension_p_a_amount, pension_p_m_amount, one_by_six_deduction, 
		salary_deduction, other_deduction, 
		total_deduction, date_paid, net_gratuity, add_additional_gratuity, 
		second_position_last_held, second_ministry_or_department,
		second_date_of_retirement, second_voucher_number, second_gratuity_amount, second_pension_p_a_amount, 
		second_pension_p_m_amount, second_one_by_six_deduction, second_salary_deduction, second_other_deduction, 
		second_total_deduction, second_date_paid, second_net_gratuity, retirement_comments, 
		gratuity_comments, start_date, end_date, timestamp, added_by, last_updated, last_updated_by, comments) 
	
	VALUES(new.id, new.employment_number, name, new.received_from_records, new.date_received_from_records, 
		new.approved_and_sumitted_to_NAO, new.date_sumitted_to_NAO, 
		new.received_from_NAO, new.date_received_from_NAO, new.approved_by_NAO_and_sumitted_to_PMO, 
		new.date_sumitted_to_PMO, new.disapproved_by_AGD_and_returned_to_ministry_or_department,
		new.disapproved_by_NAO_and_returned_to_ministry_or_department, new.date_returned_to_ministry_or_department, 
		new.position_last_held, new.ministry_or_department, 
		new.date_of_birth, new.date_of_retirement, new.voucher_number, 
		new.gratuity_amount, new.pension_p_a_amount, new.pension_p_m_amount, new.one_by_six_deduction, 
		new.salary_deduction, new.other_deduction,
		new.total_deduction, new.date_paid, new.net_gratuity, new.add_additional_gratuity, 
		new.second_position_last_held, new.second_ministry_or_department,
		new.second_date_of_retirement, new.second_voucher_number, new.second_gratuity_amount, new.second_pension_p_a_amount, 
		new.second_pension_p_m_amount, new.second_one_by_six_deduction, new.second_salary_deduction, new.second_other_deduction, 
		new.second_total_deduction, new.second_date_paid, new.second_net_gratuity, new.retirement_comments, 
		new.gratuity_comments, new.start_date, new.end_date, new.timestamp, new.added_by, new.last_updated, new.last_updated_by, new.comments);

END//
DELIMITER ;




