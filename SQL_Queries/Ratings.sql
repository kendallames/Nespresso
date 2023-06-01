-- SELECT c.CapsuleID,
-- 	c.Name,
-- 	c.Machine_Type,
--     k.KJRating
-- FROM Capsules c
-- JOIN Kendall_Ratings k
-- ON c.CapsuleID = k.CapsuleID
-- ORDER BY KJRating DESC

SELECT c.CapsuleID,
	c.Name,
	c.Machine_Type,
    k.KJRating
FROM Capsules c
JOIN Kendall_Ratings k
ON c.CapsuleID = k.CapsuleID
ORDER BY KJRating DESC

