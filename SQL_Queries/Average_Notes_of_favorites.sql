SELECT AVG(Bitterness) AS 'Average Bitterness',
	AVG(Acidity) AS 'Average Acidity',
    AVG(Roast_Level) AS 'Average Roast Level',
    AVG(Body) AS 'Average Body'
FROM (
    SELECT cp.Bitterness, cp.Acidity, cp.Roast_Level, cp.Body, k.KJRating
    FROM Capsules c
    JOIN Coffee_Profile cp 
		ON c.CapsuleID = cp.CapsuleID
    JOIN Kendall_Ratings k 
		ON c.CapsuleID = k.CapsuleID
	WHERE k.KJRating > 4
    ORDER BY k.KJRating DESC
) AS favorites;
