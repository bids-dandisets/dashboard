# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000012/blob/draft/derivatives/validations/bids_validation.txt#L46)     |          81521           |             327650              |
|   ERROR    |      [SIDECAR_KEY_REQUIRED](https://github.com/bids-dandisets///000039/blob/draft/derivatives/validations/bids_validation.txt#L96)       |          14187           |             109917              |
|  WARNING   |    [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000012/blob/draft/derivatives/validations/bids_validation.txt#L13)    |          39352           |              59239              |
|   ERROR    |   [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000638/blob/draft/derivatives/validations/bids_validation.txt#L124)   |           3584           |              13334              |
|   ERROR    |       [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L150)       |           632            |               814               |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000010/blob/draft/derivatives/validations/bids_validation.txt#L7)       |           721            |               718               |
|   ERROR    |    [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           1206           |               640               |
|  WARNING   |        [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L35)        |           316            |               436               |
|   ERROR    |         [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L134)         |           316            |               407               |
|   ERROR    |  [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000025/blob/draft/derivatives/validations/bids_validation.txt#L13)   |           384            |               384               |
|  WARNING   |         [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000010/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           366            |               364               |
|  WARNING   |           [NO_AUTHORS](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L25)            |           118            |               117               |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000019/blob/draft/derivatives/validations/bids_validation.txt#L35)        |           118            |               117               |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13) |            39            |               39                |
|   ERROR    |     [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/bids_validation.txt#L93)     |            1             |                1                |
|   ERROR    |          [NOT_INCLUDED](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/bids_validation.txt#L19)           |          35655           |                0                |
|   ERROR    |    [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)     |           346            |                0                |
|   ERROR    |      [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000056/blob/draft/derivatives/validations/bids_validation.txt#L112)      |          19727           |                0                |


## `nwb2bids` Notifications

