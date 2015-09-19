#!/usr/bin/env python

db.define_table("people",
        Field("name", "string", notnull=True, default=None),
        Field("phone", "string", notnull=True, default=None),
        Field("created_at", "datetime", default=request.now, readable=False,
            writable=False))
