# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |            Title             |                                           Count<br>(Unsanitized)                                            |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------: | :---------------------------------------------------------------------------------------------------------: | :-----------------------------: |
|   ERROR    | JSON_SCHEMA_VALIDATION_ERROR |  [4](https://github.com/bids-dandisets//001518/blob/draft/derivatives/validations/bids_validation.txt#L19)  |                0                |
|   ERROR    |   TSV_VALUE_INCORRECT_TYPE   | [48](https://github.com/bids-dandisets//001610/blob/draft/derivatives/validations/bids_validation.txt#L13)  |                0                |
|   ERROR    |         NOT_INCLUDED         | [261](https://github.com/bids-dandisets//001610/blob/draft/derivatives/validations/bids_validation.txt#L22) |                0                |
|  WARNING   |       SUBJECT_FOLDERS        |  [1](https://github.com/bids-dandisets//001518/blob/draft/derivatives/validations/bids_validation.txt#L1)   |                0                |
|  WARNING   |     JSON_KEY_RECOMMENDED     |  [2](https://github.com/bids-dandisets//001518/blob/draft/derivatives/validations/bids_validation.txt#L7)   |                0                |


## `nwb2bids` Notifications

