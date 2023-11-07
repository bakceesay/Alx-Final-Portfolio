-- TRIGGER FOR AGD MAIN STORE 

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
	IF new.issue_amount = 0 
		THEN INSERT INTO items_voucheraudit(id, last_updated, category_id, item_name_id, quantity, receive_amount, receive_by, supplier_name_id) VALUES(new.id, new.last_updated, new.category_id, new.item_name_id, new.quantity, new.receive_amount, new.receive_by, new.supplier_name_id);

	ELSEIF new.receive_amount = 0 
		THEN INSERT INTO items_voucheraudit(id, last_updated, category_id, item_name_id, issue_amount, issue_to, ministry_or_department, unit_id, issue_by, quantity) VALUES(new.id, new.last_updated, new.category_id, new.item_name_id, new.issue_amount, new.issue_to, new.ministry_or_department, new.unit_id, new.issue_by, new.quantity);
	END IF;
END//
DELIMITER ;


