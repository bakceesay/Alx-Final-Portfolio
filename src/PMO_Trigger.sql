-- TRIGGER FOR PMO

DELIMITER //
DROP TRIGGER IF EXISTS after_uimsapp_employee_insert//
CREATE TRIGGER after_uimsapp_employee_insert AFTER INSERT ON uimsapp_employee FOR EACH ROW
BEGIN
INSERT INTO uimsapp_employeeaudit (
			id, 
			passport_picture, 
            employment_number, 
            title, name, gender, 
            nationality, id_card_number, 
            home_country, residence, 
            contact_number, email_address, 
            status, status_start_date, 
            status_end_date, vocation_id, 
            vocation_start_date, 
            vocation_end_date, alert_days, 
            dob, place_of_birth, fad, cad, 
            cd, designation, budget_entity_id, 
            division, duty_station, grade, 
            grade_point, next_of_kin, qualification, 
            tin_number, marital_status, added_by, 
            updated_by, last_updated, timestamp
            )
            
		VALUES(
			new.id, 
            new.passport_picture, 
            new.employment_number, 
            new.title, new.name, new.gender, 
            new.nationality, new.id_card_number, 
            new.home_country, new.residence, 
            new.contact_number, new.email_address, 
            new.status, new.status_start_date, 
            new.status_end_date, new.vocation_id,
			new.vocation_start_date, 
            new.vocation_end_date, new.alert_days, 
            new.dob, new.place_of_birth, new.fad, new.cad, 
            new.cd, new.designation, new.budget_entity_id, 
            new.division, new.duty_station, new.grade, 
            new.grade_point, new.next_of_kin, new.qualification, 
            new.tin_number, new.marital_status, new.added_by, 
            new.updated_by, new.last_updated, new.timestamp
		);
END//
DELIMITER ;



DELIMITER //
DROP TRIGGER IF EXISTS after_uimsapp_employee_update//
CREATE TRIGGER after_uimsapp_employee_update AFTER UPDATE ON uimsapp_employee FOR EACH ROW
BEGIN
		INSERT INTO uimsapp_employeeaudit(
			id, 
			passport_picture, 
            employment_number, 
            title, name, gender, 
            nationality, id_card_number, 
            home_country, residence, 
            contact_number, email_address, 
            status, status_start_date, 
            status_end_date, vocation_id, 
            vocation_start_date, 
            vocation_end_date, alert_days, 
            dob, place_of_birth, fad, cad, 
            cd, designation, budget_entity_id, 
            division, duty_station, grade, 
            grade_point, next_of_kin, qualification, 
            tin_number, marital_status, added_by, 
            updated_by, last_updated, timestamp
		)

		VALUES(
			new.id, 
            new.passport_picture, 
            new.employment_number, 
            new.title, new.name, new.gender, 
            new.nationality, new.id_card_number, 
            new.home_country, new.residence, 
            new.contact_number, new.email_address, 
            new.status, new.status_start_date, 
            new.status_end_date, new.vocation_id,
			new.vocation_start_date, 
            new.vocation_end_date, new.alert_days, 
            new.dob, new.place_of_birth, new.fad, new.cad, 
            new.cd, new.designation, new.budget_entity_id, 
            new.division, new.duty_station, new.grade, 
            new.grade_point, new.next_of_kin, new.qualification, 
            new.tin_number, new.marital_status, new.added_by, 
            new.updated_by, new.last_updated, new.timestamp
		);
END//
DELIMITER ;



