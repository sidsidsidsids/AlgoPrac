# [Gold II] Pohlepko - 13940 

[문제 링크](https://www.acmicpc.net/problem/13940) 

### 성능 요약

메모리: 36596 KB, 시간: 2336 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 제출 일자

2024년 11월 10일 09:39:41

### 문제 설명

<p>Little Greedy got a board for his birthday. The board has N rows and M columns, and has a lowercase letter of the English alphabet​ in each field. During his birthday party, everyone got bored so they decided to play a simple board game.</p>

<p>The game begins with placing a chip on the upper left​ field labeled with coordinates (1, 1). In each turn, we must​ move the chip one field to the right or down, given the constraint that it remains on the board. The game ends with moving the chip to the lower right​ field of the board labeled with coordinates (N, M). During the game, we take note of the array of characters we form by moving the chip and therefore constructing a word. The goal of the game is to find the lexicographically smallest word.</p>

<p>The player(s) that will suceed in constructing the lexicographically smallest word get a bag of candy as a prize. Greedy wants to win the candy at any price, so he is asking you to write a programme that will find the lexicographically smallest​ possible word.</p>

<p>Please note​: The lexicographic order of words is the one in which the words appear in a dictionary. If we have two words, and the words differ in the first letter, then the smaller word is the one with the letter that comes first in the alphabet. </p>

### 입력 

 <p>The first line of input contains integers N and M, separated by space (1 ≤ N, M ≤ 2000).</p>

<p>The following N lines contains M lowercase letters of the English alphabet that represent the board. </p>

### 출력 

 <p>You must output the lexicographically smallest word. </p>

