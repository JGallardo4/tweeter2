SELECT
	UserTweets.Id AS tweetId,
	User.Id AS UserId,
	Content AS content,
	Created_At AS createdAt,
	Username AS username
FROM
	(
		SELECT
			Id,
			Username
		FROM
			Users
	) AS User
	JOIN (
		SELECT
			*
		FROM
			Tweets
		WHERE
			User_Id = X
	) AS UserTweets ON UserTweets.User_Id = User.Id