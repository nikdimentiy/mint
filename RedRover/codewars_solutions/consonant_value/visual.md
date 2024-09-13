# Visualization for "strength"

## 1. Input String
**Input:** `"strength"`

## 2. Identifying Consonant Substrings
```
s t r e n g t h
│ │ │  	│ │ │ │
└─┴─┘ 	└─┴─┴─┘
  ↓     ↓
"str" "ngth"
```

## 3. Consonant Substrings Extracted
- **"str"**
- **"ngth"**

## 4. Calculating Values for Each Substring


### a) For "str":
```
s = 19
t = 20
r = 18
Total: 19 + 20 + 18 = 57
```

### b) For "ngth":
```
n = 14
g = 7
t = 20
h = 8
Total: 14 + 7 + 20 + 8 = 49
```

## 5. Finding the Maximum Value
```
Max(19, 57, 49) = 57
```

## 6. Final Result
**Result:** **57**

## Visual Representation of the Process
```
Input: "strength"
│
├─ Consonant Substrings:
│  ├─ "str"  → 57 ◄── Highest Value
│  └─ "ngth" → 49
│
└─ Result: 57
```

Link to GitBook: https://app.gitbook.com/o/AHbYH664upZMM8d0dgms/s/JWqx9GhfRMQPD2OFaGMr/
