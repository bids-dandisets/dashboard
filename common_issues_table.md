# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|   ERROR    |    [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L103)    |           350            |                0                |
|   ERROR    |      [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L116)      |           3906           |                0                |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L35)        |            86            |                0                |
|   ERROR    |          [NOT_INCLUDED](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L42)           |           2759           |                0                |
|   ERROR    |  [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)   |           270            |                0                |
|   ERROR    |      [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000039/blob/draft/derivatives/validations/bids_validation.txt#L96)       |           1023           |                0                |
|   ERROR    |    [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)     |           330            |                0                |
|   ERROR    |   [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L124)   |           3584           |                0                |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)       |           531            |                0                |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           7668           |                0                |
|  WARNING   |    [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L70)    |           4225           |                0                |
|  WARNING   |         [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           284            |                0                |
|  WARNING   |           [NO_AUTHORS](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L25)            |            86            |                0                |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L46) |            39            |                0                |


## `nwb2bids` Notifications

