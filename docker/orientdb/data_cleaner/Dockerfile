FROM orientdb:3.2.0

# Copy custom config
COPY ./docker/orientdb/config/orientdb-server-config.xml /orientdb/config/

# Expose ports
EXPOSE 2424 2480

# Volume for databases
VOLUME /orientdb/databases

# Health check
HEALTHCHECK --interval=30s --timeout=5s \
    CMD curl -f http://localhost:2480 || exit 1