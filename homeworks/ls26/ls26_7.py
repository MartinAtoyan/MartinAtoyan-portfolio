def log_messages(level, *args, **kwargs):
    
    user = kwargs.get('user')
    
    log_header = f"User: {user}\n"
    
    log_body = "\n".join(args)

    return log_header + log_body

log_entry = log_messages( 'info', "System started successfully.", "No issues detected.", user = "admin" )

print(log_entry)
