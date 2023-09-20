READ_PERMISSION = 1 << 0  # Bit 0 (1st bit): Read permission
WRITE_PERMISSION = 1 << 1  # Bit 1 (2nd bit): Write permission
EXECUTE_PERMISSION = 1 << 2  # Bit 2 (3rd bit): Execute permission
DELETE_PERMISSION = 1 << 3  # Bit 3 (4th bit): Delete permission

user_permissions = int(input("Enter your permission bitmask as an integer: "))

has_read_permission = user_permissions & READ_PERMISSION != 0
has_write_permission = user_permissions & WRITE_PERMISSION != 0
has_execute_permission = user_permissions & EXECUTE_PERMISSION != 0
has_delete_permission = user_permissions & DELETE_PERMISSION != 0

print("User Permissions:")
print(f"Read Permission: {'Yes' if has_read_permission else 'No'}")
print(f"Write Permission: {'Yes' if has_write_permission else 'No'}")
print(f"Execute Permission: {'Yes' if has_execute_permission else 'No'}")
print(f"Delete Permission: {'Yes' if has_delete_permission else 'No'}")

# xor => either value has to be different
# || => only need 1 in a value
# & => 0 unless both value are 1
# ~ (not) => flips 0 to 1, 1 to 0

# just refer to own binary notes !!


"""
x = 15 --> 00001111
y = 16 --> 00010000

x & y = 0  (00000000)

x | y = 31 (00011111)

~x = 240 (11110000)

x ^ y = 31 (00011111)

x << 1 = 30 (00011110) (shift 1 bit to left)
x >> 2 = 3 (00000011) (shift 2 bit to right)

basically shift left increase, shift right decrease

"""
