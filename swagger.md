## `/` - **GET**
{replacethisfornow}
### Result
```json
{
    "additionalProperties": {
        "type": "string"
    },
    "type": "object"
}
```
## `/Benchmarks` - **GET**
{replacethisfornow}
### Result
```json
{
    "items": {
        "$ref": "#/components/schemas/Benchmark"
    },
    "type": "array"
}
```
## `/Birthdays` - **GET**
{replacethisfornow}
### Result
```json
{
    "items": {
        "$ref": "#/components/schemas/Birthday"
    },
    "type": "array"
}
```
## `/Economy/GetAll` - **GET**
{replacethisfornow}
### Result
```json
{
    "items": {
        "$ref": "#/components/schemas/BankAccount"
    },
    "type": "array"
}
```
## `/Economy/GetOne` - **GET**
{replacethisfornow}
### Parameters
| Name | Type |
|---|---|
| UserID | string |
### Result
```json
{
    "$ref": "#/components/schemas/BankAccount"
}
```
## `/Economy/PostOne` - **POST**
{replacethisfornow}
### Parameters
| Name | Type |
|---|---|
| UserID | string |
| Amount | double |

## `/Misc/GetAll` - **GET**
{replacethisfornow}
### Result
```json
{
    "items": {
        "$ref": "#/components/schemas/Miscellaneous"
    },
    "type": "array"
}
```
## `/Misc/GetOne` - **GET**
{replacethisfornow}
### Parameters
| Name | Type |
|---|---|
| DiscordID | string |
### Result
```json
{
    "$ref": "#/components/schemas/Miscellaneous"
}
```
## `/Misc/StreakPlusOne` - **PUT**
{replacethisfornow}
### Parameters
| Name | Type |
|---|---|
| UserID | string |

## `/Misc/PostOne` - **POST**
{replacethisfornow}
### Parameters
| Name | Type |
|---|---|
| UserID | string |
| Streak | int32 |

## `/Quotes/GetAll` - **GET**
{replacethisfornow}
### Result
```json
{
    "items": {
        "$ref": "#/components/schemas/Cite"
    },
    "type": "array"
}
```
## `/Quotes/PostOne` - **POST**
{replacethisfornow}
### Parameters
| Name | Type |
|---|---|
| discord_id | string |
| quote | string |
