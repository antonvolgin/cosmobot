.PHONY: all

all:
	echo '!!! provide param !!!'

CURDIR=$(shell pwd)
SQLITE=$(CURDIR)/database/cosmo_catalog.db
MIGRATIONSDIR=$(CURDIR)/migrations
VERSION_TABLE=_version

pack:
	# tar zcvf "$$(date +'%Y-%m-%d_%H-%M-%S').tar.gz" -T tar_list.txt
	tar zcvf dist.tar.gz -T tar_list.txt

# view:
# 	tar -tvf dist.tar.gz

target:
	scp dist.tar.gz root@95.163.243.208:/usr/local/bin/cosmocode_apiai/

# 	# tar zxvf dist.tar.gz

sql: install-goose migrationsdir
	goose --dir $(MIGRATIONSDIR) -table $(VERSION_TABLE) sqlite3 $(SQLITE) create $(name) sql

up: install-goose migrationsdir
	goose --dir $(MIGRATIONSDIR) -table $(VERSION_TABLE) sqlite3 $(SQLITE) up

down: install-goose migrationsdir
	goose --dir $(MIGRATIONSDIR) -table $(VERSION_TABLE) sqlite3 $(SQLITE) down

status: install-goose migrationsdir
	goose --dir $(MIGRATIONSDIR) -table $(VERSION_TABLE) sqlite3 $(SQLITE) status

migrationsdir:
	mkdir -p $(MIGRATIONSDIR)

install-goose:
	which goose || go install github.com/pressly/goose/v3/cmd/goose@v3.7.0
