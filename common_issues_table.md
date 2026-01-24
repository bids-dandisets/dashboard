# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                    Title                                                                     |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |       [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)       |          368575          |             216344              |
|   ERROR    |        [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L343)        |          42261           |              24912              |
|   ERROR    |      [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L294)      |          39431           |              23866              |
|   ERROR    | [TSV_ADDITIONAL_COLUMNS_MUST_DEFINE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L334) |           9024           |              5924               |
|   ERROR    |         [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L348)         |           613            |               613               |
|  WARNING   |          [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L35)          |           305            |               390               |
|   ERROR    |           [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L332)           |           305            |               305               |
|  WARNING   |         [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)         |           626            |               11                |
|   ERROR    |        [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L386)        |          18230           |                7                |
|   ERROR    |     [TSV_COLUMN_ORDER_INCORRECT](https://github.com/bids-dandisets///001675/blob/draft/derivatives/validations/bids_validation.txt#L191)     |            3             |                3                |
|  WARNING   |             [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)              |            90            |                2                |
|   ERROR    |          [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)          |            90            |                2                |
|   ERROR    |      [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L284)       |            1             |                1                |
|  WARNING   |           [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)            |           330            |                0                |
|  WARNING   |   [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13)   |            39            |                0                |
|  WARNING   |     [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000402/blob/draft/derivatives/validations/bids_validation.txt#L294)      |           327            |                0                |
|   ERROR    |            [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)             |          35814           |                0                |
|   ERROR    |    [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           364            |                0                |
|   ERROR    |      [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)       |           264            |                0                |
|   ERROR    |     [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L334)     |          29568           |                0                |


## `nwb2bids` Notifications

