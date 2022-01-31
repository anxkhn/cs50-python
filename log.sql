-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Theft on July 28, 2021 and place was Chamberlin Street.
SELECT description
FROM crime_scene_reports
WHERE day=28 AND month=7 AND year=2021 AND street="Chamberlin Street"

--Work with the description
SELECT transcript
FROM interviews
WHERE day = "28" AND month = "7" AND year = "2021" AND transcript like "%courthouse%"

--first transcripts.
--"Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse
--parking lot and drive away. If you have security footage from the courthouse parking lot,
--you might want to look for cars that left the parking lot in that time frame."
SELECT name
FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE day = "28" AND month = "7" AND year = "2021" AND hour = "10" AND minute >= "15" AND minute < "25" AND activity = "exit"

--Patrick, Ernest, Amber, Danielle, Roger, Elizabeth, Russel, Evelyn

--second transcript:
--"I don't know the thief's name, but it was someone I recognized. Earlier this morning,
--before I arrived at the courthouse, I was walking by the ATM on Fifer Street and saw
--the thief there withdrawing some money."
SELECT DISTINCT name
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE day = "28" AND month = "7" AND year = "2021" AND transaction_type = "withdraw" AND atm_location = "Fifer Street"

--Danielle, Bobby, Madison, Ernest, Roy, Elizabeth, Victoria, Russel

--Overlap: Ernest, Danielle, Elizabeth, Russel

--third transcript:
--"As the thief was leaving the courthouse, they called someone who talked to them for less than a minute.
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville
--tomorrow.The thief then asked the person on the other end of the phone to purchase the flight ticket."
--check flight
SELECT name
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = (
    SELECT id
    FROM flights
    WHERE day = "29" AND month = "7" AND year = "2021"
    ORDER BY hour, minute
    LIMIT 1)
--Doris, Roger, Ernest, Edward, Evelyn, Madison, Bobby, Danielle
--Final lists: Ernest and Danielle

--Check the phonebook
SELECT DISTINCT name
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE day = "28" AND month = "7" AND year = "2021" AND duration < "60"
--Roger, Evelyn, Ernest, Madison, Russell, Kimberly, Bobby, Victoria

--Ernest overlaps.

SELECT city
FROM airports
WHERE id = (
    SELECT destination_airport_id
    FROM flights
    WHERE day = "29" AND month = "7" AND year = "2021"
    ORDER BY hour, minute
    LIMIT 1)
--Location: London

--ACCOMPLICE
SELECT name
FROM people
JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE day = "28" AND month = "7" AND year = "2021" AND duration < "60" AND caller = (
    SELECT phone_number
    FROM people
    WHERE name = "Ernest");
--The ACCOMPLICE is: Berthold