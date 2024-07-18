CREATE TABLE `User` (
    `UserID` int  NOT NULL ,
    `Username` string  NOT NULL ,
    `Email` string  NOT NULL ,
    PRIMARY KEY (
        `UserID`
    )
);

CREATE TABLE `TextCreated` (
    `TextCreatedID` int  NOT NULL ,
    `UserID` int  NOT NULL ,
    `MetaDataUsed` string  NOT NULL ,
    PRIMARY KEY (
        `TextCreatedID`
    )
);

CREATE TABLE `BookData` (
    `BookDataID` int  NOT NULL ,
    `Authors` string  NOT NULL ,
    `Title` string  NOT NULL ,
    `Year` int  NOT NULL ,
    `Subjects` string  NOT NULL ,
    `Bookshelves` string  NOT NULL ,
    `Copyright` Boolean  NOT NULL ,
    PRIMARY KEY (
        `BookDataID`
    )
);

CREATE TABLE `LineFetched` (
    `LineFetchedID` int  NOT NULL ,
    `BookDataID` int  NOT NULL ,
    `Excerpt` text  NOT NULL ,
    PRIMARY KEY (
        `LineFetchedID`
    )
);

CREATE TABLE `LineStamped` (
    `LineStampedID` int  NOT NULL ,
    `TextCreatedID` int  NOT NULL ,
    `LineFetchedID` int  NOT NULL ,
    PRIMARY KEY (
        `LineStampedID`
    )
);

ALTER TABLE `TextCreated` ADD CONSTRAINT `fk_TextCreated_UserID` FOREIGN KEY(`UserID`)
REFERENCES `User` (`UserID`);

ALTER TABLE `LineFetched` ADD CONSTRAINT `fk_LineFetched_BookDataID` FOREIGN KEY(`BookDataID`)
REFERENCES `BookData` (`BookDataID`);

ALTER TABLE `LineStamped` ADD CONSTRAINT `fk_LineStamped_TextCreatedID` FOREIGN KEY(`TextCreatedID`)
REFERENCES `TextCreated` (`TextCreatedID`);

ALTER TABLE `LineStamped` ADD CONSTRAINT `fk_LineStamped_LineFetchedID` FOREIGN KEY(`LineFetchedID`)
REFERENCES `LineFetched` (`LineFetchedID`);

CREATE INDEX `idx_User_Username`
ON `User` (`Username`);

