-- computes and store the weighted average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users
    SET average_score = (SELECT SUM(score * projects.weight)/SUM(projects.weight) FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id);
END
$$
DELIMITER ;
