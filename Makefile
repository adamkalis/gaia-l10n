# adapt to your local configuration
GAIA_MAINDIR ?= ~/www/gaia
GAIA_APPDIRS ?= apps showcase_apps test_apps

# get the list of all internationalized Gaia apps
# TODO: it'd be nice if it was sorted...
GAIA_APPS = `find -L ${GAIA_APPDIRS} -mindepth 1 -maxdepth 1 -type d`
GAIA_APPS += apps/communications/dialer
GAIA_APPS += apps/communications/contacts

# copy resources from this l10n directory to the main Gaia directory
export:
	@for app in ${GAIA_APPS}; do                                                \
		echo "$$app";                                                             \
		cp $$app/manifest.webapp $(GAIA_MAINDIR)/$$app/;                          \
		if [ -d "$$app/locales" ]; then                                           \
			cp $$app/locales/* $(GAIA_MAINDIR)/$$app/locales/;                      \
		fi;                                                                       \
	done

# copy resources from the main Gaia directory to this l10n directory
import:
	@for app in ${GAIA_APPS}; do                                                \
		echo "$$app";                                                             \
		cp $(GAIA_MAINDIR)/$$app/manifest.webapp $$app/;                          \
		if [ -d "$$app/locales" ]; then                                           \
			cp $(GAIA_MAINDIR)/$$app/locales/* $$app/locales/;                      \
		fi;                                                                       \
	done

# list all internationalized Gaia apps
define l10n-list
	for d in ${GAIA_APPS}; do                                                   \
		echo $$d;                                                                 \
	done
endef
list:
	$(call l10n-list) | sort

