-- 코드를 입력하세요
SELECT user.USER_ID as USER_ID, user.NICKNAME as NICKNAME, SUM(board.PRICE) as TOTAL_SALES
FROM USED_GOODS_USER user
LEFT JOIN USED_GOODS_BOARD as board ON user.USER_ID = board.WRITER_ID WHERE board.STATUS = 'DONE'
GROUP BY board.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES