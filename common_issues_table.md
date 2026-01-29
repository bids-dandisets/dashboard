# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                    Title                                                                     |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |       [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L46)       |          259067          |             115336              |
|   ERROR    |      [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L327)      |           1306           |              17750              |
|   ERROR    |        [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L340)        |          29625           |              13308              |
|   ERROR    | [TSV_ADDITIONAL_COLUMNS_MUST_DEFINE](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L179) |            3             |              4438               |
|   ERROR    |        [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L383)        |          19793           |                7                |
|   ERROR    |         [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L348)         |           613            |                3                |
|   ERROR    |     [TSV_COLUMN_ORDER_INCORRECT](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L191)     |            3             |                3                |
|  WARNING   |         [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)         |           671            |                2                |
|   ERROR    |  [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/basic_sanitization/derivatives/validations/bids_validation.txt#L284)   |            0             |                1                |
|   ERROR    |            [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)             |          36219           |                0                |
|   ERROR    |          [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)          |           100            |                0                |
|   ERROR    |    [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           376            |                0                |
|   ERROR    |      [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)       |           264            |                0                |
|   ERROR    |     [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L325)     |          29568           |                0                |
|   ERROR    |           [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L332)           |           305            |                0                |
|  WARNING   |      [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)      |          18403           |                0                |
|  WARNING   |           [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)            |           347            |                0                |
|  WARNING   |             [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)              |           100            |                0                |
|  WARNING   |   [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13)   |            39            |                0                |
|  WARNING   |          [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L35)          |           305            |                0                |


## `nwb2bids` Notifications

