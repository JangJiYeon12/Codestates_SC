"""
Part 1.1
데이터베이스를 스키마대로 생성해야 합니다.
테이블을 생성하는 3개의 구문을 작성하세요.
"""



CREATE_USER_TABLE = """
CREATE TABLE User(
	id INTEGER NOT NULL PRIMARY KEY,
	username VARCHAR(8000),
	password VARCHAR(8000)
);
"""

CREATE_PRODUCT_TABLE = """
CREATE TABLE Product(
	id INTEGER NOT NULL PRIMARY KEY,
	product_name VARCHAR(8000),
	product_price INTEGER
);
"""

CREATE_USER_PRODUCT_TABLE = """
CREATE TABLE User_Product(
	id INTEGER,
	user_id INTEGER,
	product_id INTEGER,
	FOREIGN KEY(user_id) REFERENCES User(id),
	FOREIGN KEY(product_id) REFERENCES Product(id)
);
"""

"""
Part 1.2

각 질문에 해당하는 결과를 조회할 수 있는 SQL 쿼리문을 작성합니다.
"""

# 1. 데이터베이스에서 가장 비싼 제품 (개별 가격당) 10개를 구해보세요.
# - 제품 이름만 쿼리 결과에 포함합니다.
SQL_QUERY_1 = """
SELECT p.ProductName FROM Product p
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""

# 2. 고용 당시 직원의 평균 연령을 구해보세요.
SQL_QUERY_2 = "SELECT SUM(e.HireDate - e.BirthDate) / 9 FROM Employee e;"

# 3. 1번 문제에 제품을 만든 회사들도 같이 구해보세요.
# - 제품 id, 제품 이름, 유닛 가격, 회사 이름만 쿼리 결과에 포함합니다.
SQL_QUERY_3 = """
SELECT p.id, p.ProductName, p.UnitPrice, s.CompanyName FROM Product p
JOIN Supplier s ON p.id = s.id
ORDER BY p.UnitPrice DESC
LIMIT 10;
"""

# 4. 제품의 종류를 가장 많이 가지고 있는 카테고리는 무엇일까요? (카테고리 이름 하나만 출력합니다)
SQL_QUERY_4 = "SQL 쿼리문을 작성해 주세요."

# 5. 각 도시별로 직원의 고용 당시 평균 연령을 구해보세요.
# - 도시 이름과 도시별 평균 연령을 쿼리 결과에 포함합니다.
SQL_QUERY_5 = "SELECT AVG(e.HireDate - e.BirthDate), e.City FROM Employee e GROUP BY e.City;"

# 6. 어느 직원이 가장 많은 영역(Territory)을 차지하고 있나요?
# - 직원 id, 직원 Lastname, 총 영역 수를 쿼리 결과에 포함합니다.
SQL_QUERY_6 = """
SELECT e.Id, e.LastName, count(*) FROM EmployeeTerritory et
JOIN Employee e ON et.EmployeeId = e.Id 
GROUP BY et.EmployeeId
;
"""
