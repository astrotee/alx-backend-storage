-- Add bonus
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
  IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
    INSERT INTO projects ( name ) VALUES ( project_name );
    SET @pid = LAST_INSERT_ID();
  ELSE
    SET @pid = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
  END IF;
  INSERT INTO corrections  VALUES ( user_id, @pid, score );
END
$$
DELIMITER ;
