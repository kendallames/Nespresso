SELECT c.CapsuleID AS ID,
    c.Name,
    k.KJRating AS 'KJ Rating',
    c.Machine_Type
FROM Kendall_Ratings k
JOIN Capsules c
	WHERE k.CapsuleID = c.CapsuleID
ORDER BY KJRating DESC