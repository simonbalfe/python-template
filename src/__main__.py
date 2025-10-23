from .main import user1, user2, collection, math_op, result

def main():
    print(f"User info: {user1.get_info()}")
    print(f"Total users: {collection.total_count}")
    print(f"Math result: {result}")

if __name__ == "__main__":
    main()
