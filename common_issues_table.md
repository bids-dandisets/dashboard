# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                    Title                                                                     |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |       [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)       |          368677          |             157617              |
|  WARNING   |     [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L294)      |          32688           |              21922              |
|   ERROR    |        [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L348)        |          42258           |              18171              |
|   ERROR    |      [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L327)      |           1319           |               182               |
|  WARNING   |         [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L316)          |           316            |               85                |
|  WARNING   |         [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)         |           701            |                7                |
|   ERROR    |        [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L340)        |          19842           |                7                |
|   ERROR    |         [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L391)         |           635            |                3                |
|   ERROR    |     [TSV_COLUMN_ORDER_INCORRECT](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L202)     |            3             |                3                |
|   ERROR    | [TSV_ADDITIONAL_COLUMNS_MUST_DEFINE](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L214) |            3             |                3                |
|  WARNING   |             [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)              |           107            |                1                |
|   ERROR    |      [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L317)       |            1             |                1                |
|   ERROR    |          [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)          |           107            |                1                |
|  WARNING   |           [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)            |           360            |                0                |
|  WARNING   |   [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L46)   |            39            |                0                |
|   ERROR    |            [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)             |          36219           |                0                |
|   ERROR    |    [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           380            |                0                |
|   ERROR    |      [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)       |           264            |                0                |
|   ERROR    |     [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L368)     |          29568           |                0                |
|   ERROR    |           [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L383)           |           316            |                0                |


## `nwb2bids` Notifications

