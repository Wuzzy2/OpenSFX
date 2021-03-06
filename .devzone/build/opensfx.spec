
Name:           %{dz_repo}
Version:        %{dz_version}
%define srcver  %{version}
Release:        %{_vendor}%{?suse_version}
Summary:        OpenSFX replacement sounds for OpenTTD

Group:          Amusements/Games
License:        Creative Commons Sampling Plus 1.0
URL:            http://dev.openttdcoop.org/projects/opensfx
Source0:        %{name}-%{srcver}.tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

BuildRequires:  catcodec mercurial p7zip

Provides:       openttd-%{name} openttd-data-%{name}

%description
OpenSFX replacement sounds for OpenTTD. The last required step
to make OpenTTD independent.. 

%prep
%setup -qn %{name}
# DevZone stuff:
case %{version} in
        r*)     ;;
        *)      hg update %{version}
esac

%build
make
# following make needed for DevZone building only:
make bundle_src bundle_zip ZIP="7za a" ZIP_FLAGS="-tzip -mx9" 1>%{name}-%{version}-build.log 2>%{name}-%{version}-build.err.log 

%install
make install INSTALL_DIR=%{buildroot}%{_datadir}/openttd/data/

%clean

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%dir %{_datadir}/openttd
%dir %{_datadir}/openttd/data
%{_datadir}/openttd/data/opensfx*.tar

%changelog

