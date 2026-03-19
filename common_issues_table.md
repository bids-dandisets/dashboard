# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)     |          70830           |             333215              |
|   ERROR    |      [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000039/blob/draft/derivatives/validations/bids_validation.txt#L96)       |          12999           |             109917              |
|  WARNING   |    [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L70)    |          29623           |              60511              |
|   ERROR    |   [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L124)   |           3584           |              13334              |
|   ERROR    |  [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L124)  |           7050           |              11419              |
|   ERROR    |       [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L141)       |           4561           |              7288               |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)       |           740            |               720               |
|   ERROR    |    [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L103)    |           1210           |               642               |
|  WARNING   |       [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L118)        |           316            |               436               |
|   ERROR    |         [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L185)         |           316            |               407               |
|  WARNING   |         [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           375            |               365               |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L46) |            39            |               232               |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L35)        |           125            |               115               |
|  WARNING   |           [NO_AUTHORS](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L25)            |           125            |               115               |
|   ERROR    |     [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L93)     |            1             |                1                |
|   ERROR    |      [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L116)      |          19821           |                0                |
|   ERROR    |          [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)           |          31829           |                0                |
|   ERROR    |    [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)     |           346            |                0                |


## `nwb2bids` Notifications

