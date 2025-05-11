FROM orientdb:3.2.0

# Copy custom config
COPY ./config/orientdb-server-config.xml /orientdb/config/

# Expose ports and declare volume
EXPOSE 2424 2480
VOLUME /orientdb/databases

# (Optional) Add health check
HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:2480 || exit 1