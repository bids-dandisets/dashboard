# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                 Title                                                                 |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :-----------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |        [SUBJECT_FOLDERS](https://github.com/bids-dandisets///001626/blob/draft/derivatives/validations/bids_validation.txt#L1)        |            27            |                0                |
|  WARNING   |     [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///001626/blob/draft/derivatives/validations/bids_validation.txt#L7)      |            56            |                0                |
|  WARNING   |          [NO_AUTHORS](https://github.com/bids-dandisets///001632/blob/draft/derivatives/validations/bids_validation.txt#L31)          |            11            |                0                |
|  WARNING   |  [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///001676/blob/draft/derivatives/validations/bids_validation.txt#L13)   |           1450           |                0                |
|  WARNING   |   [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///001676/blob/draft/derivatives/validations/bids_validation.txt#L40)    |           1800           |                0                |
|   ERROR    | [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///001626/blob/draft/derivatives/validations/bids_validation.txt#L19) |            16            |                0                |
|   ERROR    |      [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///001632/blob/draft/derivatives/validations/bids_validation.txt#L41)       |            11            |                0                |
|   ERROR    |   [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///001641/blob/draft/derivatives/validations/bids_validation.txt#L13)   |            33            |                0                |
|   ERROR    |         [NOT_INCLUDED](https://github.com/bids-dandisets///001641/blob/draft/derivatives/validations/bids_validation.txt#L22)         |           160            |                0                |
|   ERROR    |    [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///001676/blob/draft/derivatives/validations/bids_validation.txt#L106)     |           1792           |                0                |
|   ERROR    |     [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///001712/blob/draft/derivatives/validations/bids_validation.txt#L90)     |            6             |                0                |


## `nwb2bids` Notifications

