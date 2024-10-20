-- Email validation to sent
-- reset valid_email on email change
DELIMITER ;;
CREATE TRIGGER rst_vemail
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;
;;
DELIMITER ;
