# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   | [TSV_ADDITIONAL_COLUMNS_UNDEFINED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#30) |           234            |               234               |
|   ERROR    |       [REQUIRED_COORDSYSTEM](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#99)       |           101            |               101               |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#17)      |            63            |               63                |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#1)        |            10            |                5                |
|  WARNING   |          [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#1)          |            4             |                4                |
|   ERROR    |     [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#78)     |            18            |                2                |
|   ERROR    |     [PARTICIPANT_ID_MISMATCH](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#66)      |            1             |                1                |
|   ERROR    |    [TSV_INDEX_VALUE_NOT_UNIQUE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#73)    |            1             |                1                |


## `nwb2bids` Notifications

|            Severity            |                                                                     Title                                                                      |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :----------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
| SCHEMA_INVALIDATION (CRITICAL) |     [Missing participant sex](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#3)     |           101            |               101               |
|    STYLE_SUGGESTION (ERROR)    |      [Invalid session ID](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#1431)      |            93            |               93                |
|     INTERNAL_ERROR (INFO)      | [INFO: invalid Dandiset metadata](https://github.com/bids-dandisets///000005/blob/draft/derivatives/validations/nwb2bids_notifications.json#3) |            3             |                3                |
|  SCHEMA_INVALIDATION (ERROR)   |       [Invalid species](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#1417)        |            1             |                1                |
