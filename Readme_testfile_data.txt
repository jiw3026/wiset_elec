testfile1은
VOLT1에 전압 강하로 전류가 많이 흘러 화재 발생 위험이 있음을 나타낸 임시 데이터 입니다.
고장을 일부러 발생 시켰습니다.

VOLT1 field 의 행 246 부터 고장 구간 입니다.

행 246 -(minus) 행 247 
행 246 -(minus) 행 248
행 246 -(minus) 행 249 

제곱, abs계산 - 오차계산의 합 / 고장 행의 갯수 계산

이런식으로 행 270까지가 고장 구간임을 인지하고 결과값은
VOLT1에 연결된 기기가 고장났음을 표시할 수 있어야 하기에 "VOLT1"을 detection 하는 내용입니다.

testfile2는 VOLT2 기준이기에 VOLT2가 고장임을 detection 할 수 있어야 합니다.
마찬가지로 testfile3는 VOLT3 기준이기에 VOLT3가 고장임을 detection 할 수 있어야 합니다.


