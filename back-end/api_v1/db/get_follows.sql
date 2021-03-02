SELECT
	follower.Follower_Username AS Follower,
	followee_Username AS Followee
FROM
	(
		SELECT
			u.Username AS Follower_Username,
			uf.Id AS Uf_Id
		FROM
			Followings AS uf
			JOIN Users AS u ON uf.Follower_Id = u.Id
	) AS follower
	JOIN (
		SELECT
			u.Username AS Followee_Username,
			uf.Id AS Uf_Id
		FROM
			Followings AS uf
			JOIN Users AS u ON uf.Followed_Id = u.Id
	) AS followee ON follower.Uf_Id = followee.Uf_Id