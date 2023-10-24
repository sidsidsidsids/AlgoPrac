-- 코드를 입력하세요
SELECT DISTINCT user.USER_ID, user.NICKNAME, CONCAT(user.CITY, " ", user.STREET_ADDRESS1, " ", user.STREET_ADDRESS2) as "전체주소", 
CASE
    WHEN LENGTH(user.TLNO) = 10 THEN
      CONCAT(
        SUBSTRING(user.TLNO, 1, 3), '-', 
        SUBSTRING(user.TLNO, 4, 3), '-', 
        SUBSTRING(user.TLNO, 7, 4)
      )
    WHEN LENGTH(user.TLNO) = 11 THEN
      CONCAT(
        SUBSTRING(user.TLNO, 1, 3), '-', 
        SUBSTRING(user.TLNO, 4, 4), '-', 
        SUBSTRING(user.TLNO, 8, 4)
      )
END AS "전화번호"
FROM USED_GOODS_USER as user RIGHT JOIN USED_GOODS_BOARD as board ON user.USER_ID = board.WRITER_ID
WHERE user.USER_ID IN (
  SELECT WRITER_ID
  FROM USED_GOODS_BOARD
  GROUP BY WRITER_ID
  HAVING COUNT(WRITER_ID) >= 3
)
ORDER BY user.USER_ID desc;