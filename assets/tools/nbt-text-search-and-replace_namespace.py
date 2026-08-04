import argparse
import os
import nbtlib


def replace_namespace(value, old_ns, new_ns):
    """Replace namespace prefix (e.g., 'minecraft:path/to' -> 'new_ns:path/to')."""
    val_str = str(value)
    target_prefix = f"{old_ns}:"

    if val_str.startswith(target_prefix):
        new_str = val_str.replace(target_prefix, f"{new_ns}:", 1)
        # Preserve original NBT String type if applicable
        return nbtlib.String(new_str) if isinstance(value, nbtlib.String) else new_str

    return value


def process_nbt_pool(data, search_vals, replace_ns=None, path=""):
    """
    Recursively traverse NBT data searching for key 'pool'.
    Returns (matches_list, modified_flag).
    """
    matches = []
    modified = False

    # Handle Compound (Dict-like) tags
    if isinstance(data, nbtlib.Compound):
        for key, value in list(data.items()):
            current_path = f"{path}.{key}" if path else key

            if key.lower() == "pool":
                val_str = str(value).lower()
                
                # Check if ANY of the search values match
                if any(s_val.lower() in val_str for s_val in search_vals):
                    matches.append((current_path, value))

                    # Perform replacement if requested
                    if replace_ns:
                        from_ns, to_ns = replace_ns
                        updated_val = replace_namespace(value, from_ns, to_ns)

                        if updated_val != value:
                            data[key] = updated_val
                            modified = True
                            matches.append((f"{current_path} (UPDATED)", updated_val))

            # Recurse down nested tags
            sub_matches, sub_mod = process_nbt_pool(value, search_vals, replace_ns, current_path)
            matches.extend(sub_matches)
            if sub_mod:
                modified = True

    # Handle List (Array-like) tags
    elif isinstance(data, nbtlib.List):
        for index, item in enumerate(data):
            current_path = f"{path}[{index}]"
            sub_matches, sub_mod = process_nbt_pool(item, search_vals, replace_ns, current_path)
            matches.extend(sub_matches)
            if sub_mod:
                modified = True

    return matches, modified


def run():
    parser = argparse.ArgumentParser(
        description="Find and optionally replace namespaces in 'pool' NBT tags across a directory."
    )
    parser.add_argument(
        "--dir", required=True, help="Target directory containing .nbt files"
    )
    parser.add_argument(
        "--search-val",
        action="append",
        required=True,
        help="Value to search for inside 'pool' keys. Can be specified multiple times.",
    )
    parser.add_argument(
        "--replace-namespace",
        nargs=2,
        metavar=("FROM", "TO"),
        help="Replace namespace prefix in matching pool tags (e.g. --replace-namespace minecraft my_mod)",
    )

    args = parser.parse_args()

    found_any = False

    for root, _, files in os.walk(args.dir):
        for file in files:
            if file.endswith((".nbt", ".dat")):
                file_path = os.path.join(root, file)

                try:
                    nbt_file = nbtlib.load(file_path)
                    matches, is_modified = process_nbt_pool(
                        nbt_file, args.search_val, args.replace_namespace
                    )

                    if matches:
                        found_any = True
                        print(f"\n📁 File: {file_path}")
                        for path, val in matches:
                            print(f"  └─ Path: {path} = {val}")

                        if is_modified:
                            nbt_file.save()
                            print("  💾 Changes saved to file.")

                except Exception as e:
                    # Silently ignore non-NBT or corrupt files
                    continue

    if not found_any:
        print(f"No matches found for search values: {args.search_val}")


if __name__ == "__main__":
    run()