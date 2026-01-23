# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                    Title                                                                     |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |       [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)       |          58808           |             216344              |
|   ERROR    |        [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L343)        |           6606           |              24912              |
|   ERROR    |         [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L226)         |            3             |               613               |
|  WARNING   |      [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///000016/basic_sanitization/derivatives/validations/bids_validation.txt#L13)      |            0             |               390               |
|   ERROR    |       [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/basic_sanitization/derivatives/validations/bids_validation.txt#L332)       |            0             |               305               |
|   ERROR    |      [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L294)      |           8678           |               178               |
|  WARNING   |         [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)         |           621            |               18                |
|   ERROR    |        [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L386)        |           7432           |                7                |
|   ERROR    |          [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)          |            92            |                4                |
|   ERROR    |    [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           376            |                4                |
|  WARNING   |             [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)              |            92            |                4                |
|   ERROR    | [TSV_ADDITIONAL_COLUMNS_MUST_DEFINE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L334) |           1512           |                3                |
|   ERROR    |     [TSV_COLUMN_ORDER_INCORRECT](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L191)     |            3             |                3                |
|  WARNING   |           [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)            |           339            |                3                |
|   ERROR    |  [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/basic_sanitization/derivatives/validations/bids_validation.txt#L284)   |            0             |                1                |
|   ERROR    |            [NOT_INCLUDED](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L22)             |           4516           |                0                |
|   ERROR    |      [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)       |           252            |                0                |
|   ERROR    |     [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L334)     |          29568           |                0                |
|  WARNING   |   [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13)   |            39            |                0                |
|  WARNING   |     [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000402/blob/draft/derivatives/validations/bids_validation.txt#L294)      |            48            |                0                |


## `nwb2bids` Notifications

