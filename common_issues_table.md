# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                    Title                                                                     |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |       [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)       |          368709          |             513199              |
|   ERROR    |        [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L382)        |          42276           |              58653              |
|   ERROR    |     [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L355)     |          14784           |              14784              |
|   ERROR    |      [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L294)      |           6486           |              11477              |
|   ERROR    |         [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L334)         |           3979           |              8487               |
|   ERROR    | [TSV_ADDITIONAL_COLUMNS_MUST_DEFINE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L355) |           3706           |              8461               |
|   ERROR    |     [TSV_COLUMN_ORDER_INCORRECT](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L425)     |           3369           |              7695               |
|   ERROR    |        [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L446)        |          16395           |              1010               |
|   ERROR    |            [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)             |          36027           |               941               |
|  WARNING   |         [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)         |           667            |               663               |
|  WARNING   |          [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L35)          |           305            |               425               |
|  WARNING   |     [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000402/blob/draft/derivatives/validations/bids_validation.txt#L294)      |           327            |               402               |
|   ERROR    |           [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L332)           |           305            |               396               |
|   ERROR    |    [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           372            |               392               |
|  WARNING   |   [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13)   |            39            |               352               |
|  WARNING   |           [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)            |           344            |               345               |
|  WARNING   |             [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)              |            99            |               98                |
|   ERROR    |          [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)          |            99            |               98                |
|   ERROR    |      [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L284)       |            1             |                1                |
|   ERROR    |      [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)       |           162            |                0                |


## `nwb2bids` Notifications

