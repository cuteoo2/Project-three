

CREATE TABLE EVStations (
    StationName VARCHAR,
    Date1 DATE,
    P_time TIME,
    Port_Type VARCHAR,
    Port_Number INT,
    Plug_Type VARCHAR,
    EVSE_ID FLOAT,
    Address1 VARCHAR,
    City VARCHAR,
    State VARCHAR,
    Postal_Code INT,
    Country VARCHAR,
    Latitude DECIMAL,
    Longitude DECIMAL,
    County VARCHAR
);

SELECT * From EVStations

Drop Table EVStations


SELECT * From EVStations

SELECT StationName, AVG (Latitude) , AVG (Longitude) FROM EVStations GROUP BY StationName
SELECT StationName, AVG (Port_Type)



