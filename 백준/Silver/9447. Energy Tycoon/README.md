# [Silver V] Energy Tycoon - 9447 

[문제 링크](https://www.acmicpc.net/problem/9447) 

### 성능 요약

메모리: 31120 KB, 시간: 60 ms

### 분류

그리디 알고리즘, 구현, 시뮬레이션

### 제출 일자

2024년 9월 14일 12:07:43

### 문제 설명

<p>Little Vasya is playing a new computer game — turn-based strategy “Energy Tycoon”.</p>

<p>The rules of the game are quite simple:</p>

<ul>
	<li>The board contains n slots arranged in a line.</li>
	<li>There are power plants, one power plant occupies one or two consecutive slots, and produces one unit of energy.</li>
	<li>Each turn the game allows you to build one new power plant, you can put it on the board if you wish. If there is no place for the new power plant, you can remove some older power plants.</li>
	<li>After each turn, the computer counts the amount of energy produced by the power plants on the board and adds it to the total score.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/enegrgytycoon.png" style="height:54px; width:545px"></p>

<p>Vasya already knows the types of power plant he will be able to build each turn. Now he wants to know, what the maximum possible score he can get is. Can you help him?</p>

### 입력 

 <p>The first line of the input contains one integer n (1 ≤ n ≤ 100 000) — the number of slots on the board. The second line contains the string s. The i-th character of the string is 1 if you can build one-slot power plant at the i-th turn and the character is 2 if you can build two-slot power plant at the i-th turn. The number of turns does not exceed 100 000.</p>

### 출력 

 <p>The output should contain a single integer — the maximal score that can be achieved.</p>

