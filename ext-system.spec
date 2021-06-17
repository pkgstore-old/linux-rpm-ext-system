%global d_bin                   %{_bindir}
%global d_home                  /home

%global d_storage_00            %{d_home}/storage.00
%global d_app                   %{d_storage_00}/app
%global d_usr                   %{d_storage_00}/usr
%global d_web                   %{d_storage_00}/web

%global d_storage_01            %{d_home}/storage.01
%global d_data_00               %{d_storage_01}/data.00
%global d_data_01               %{d_storage_01}/data.01
%global d_data_02               %{d_storage_01}/data.02
%global d_data_03               %{d_storage_01}/data.03
%global d_data_04               %{d_storage_01}/data.04
%global d_data_05               %{d_storage_01}/data.05
%global d_data_06               %{d_storage_01}/data.06
%global d_data_07               %{d_storage_01}/data.07
%global d_data_08               %{d_storage_01}/data.08
%global d_data_09               %{d_storage_01}/data.09
%global d_data_99               %{d_storage_01}/data.99

%global d_sysctl                %{_sysconfdir}/sysctl.d

%global release_prefix          100

Name:                           ext-system
Version:                        1.0.10
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for configure system
License:                        MIT

Source10:                       00-sysctl.custom.conf

Requires:                       wget zsh

%description
META-package for configure system.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

# Directory: app.
%{__install} -dp -m 0755 %{buildroot}%{d_app}

# Directory: usr.
%{__install} -dp -m 0755 %{buildroot}%{d_usr}

# Directory: web.
%{__install} -dp -m 0755 %{buildroot}%{d_web}

# Directory: data.00.
%{__install} -dp -m 0755 %{buildroot}%{d_data_00}

# Directory: data.01.
%{__install} -dp -m 0755 %{buildroot}%{d_data_01}

# Directory: data.02.
%{__install} -dp -m 0755 %{buildroot}%{d_data_02}

# Directory: data.03.
%{__install} -dp -m 0755 %{buildroot}%{d_data_03}

# Directory: data.04.
%{__install} -dp -m 0755 %{buildroot}%{d_data_04}

# Directory: data.05.
%{__install} -dp -m 0755 %{buildroot}%{d_data_05}

# Directory: data.06.
%{__install} -dp -m 0755 %{buildroot}%{d_data_06}

# Directory: data.07.
%{__install} -dp -m 0755 %{buildroot}%{d_data_07}

# Directory: data.08.
%{__install} -dp -m 0755 %{buildroot}%{d_data_08}

# Directory: data.09.
%{__install} -dp -m 0755 %{buildroot}%{d_data_09}

# Directory: data.99.
%{__install} -dp -m 2775 %{buildroot}%{d_data_99}

# Install: configs.
%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_sysctl}/00-sysctl.custom.conf

%files
# Directory: storage_00.
%dir %{d_storage_00}
%dir %{d_app}
%dir %{d_usr}
%dir %{d_web}

# Directory: storage_01.
%dir %{d_storage_01}
%dir %{d_data_00}
%dir %{d_data_01}
%dir %{d_data_02}
%dir %{d_data_03}
%dir %{d_data_04}
%dir %{d_data_05}
%dir %{d_data_06}
%dir %{d_data_07}
%dir %{d_data_08}
%dir %{d_data_09}
%dir %{d_data_99}

# Configs.
%config %{d_sysctl}/00-sysctl.custom.conf


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.10-100
- UPD: Move to GitHub.
- UPD: License.

* Tue Dec 03 2019 Package Store <kitsune.solar@gmail.com> - 1.0.9-100
- NEW: "data.99" directory.

* Mon Nov 18 2019 Package Store <kitsune.solar@gmail.com> - 1.0.8-100
- UPD: SPEC-file.

* Tue Nov 12 2019 Package Store <kitsune.solar@gmail.com> - 1.0.7-100
- UPD: Directory names.

* Sat Oct 19 2019 Package Store <kitsune.solar@gmail.com> - 1.0.6-100
- UPD: SPEC-file.
- DEL: Scripts.

* Sun Aug 04 2019 Package Store <kitsune.solar@gmail.com> - 1.0.5-100
- NEW: USB install script.
- UPD: Shell scripts.

* Fri Aug 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.4-104
- UPD: Shell scripts.

* Thu Aug 01 2019 Package Store <kitsune.solar@gmail.com> - 1.0.4-103
- UPD: Shell scripts.

* Thu Aug 01 2019 Package Store <kitsune.solar@gmail.com> - 1.0.4-102
- UPD: Shell scripts.

* Wed Jul 31 2019 Package Store <kitsune.solar@gmail.com> - 1.0.4-101
- UPD: SPEC-file.

* Mon Jul 22 2019 Package Store <kitsune.solar@gmail.com> - 1.0.4-100
- NEW: "run.sum.sh".

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-110
- UPD: Shell scripts.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-109
- UPD: Shell scripts.

* Sat Jul 06 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-108
- UPD: Shell scripts.

* Sat Jul 06 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-107
- UPD: "run.domain.sh".

* Sat Jul 06 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-106
- UPD: "run.acme.sh".

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-105
- UPD: Shell scripts.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-104
- UPD: "run.acme.sh".

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-103
- UPD: SPEC-file.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-102
- UPD: Shell scripts.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-101
- FIX: Shell scripts.
- FIX: sysctl.

* Thu Jul 04 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-100
- NEW: Shell scripts.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-104
- UPD: SPEC-file.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-103
- UPD: Directory structure.

* Sun Apr 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-102
- UPD: Directory structure.

* Sun Apr 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-101
- UPD: Directory structure.

* Sun Apr 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- UPD: Directory structure.
- DEL: System scripts.

* Sun Apr 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-101
- UPD: Directory structure.

* Sat Apr 13 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: Directory structure.
- NEW: User "sys_backup".

* Sat Apr 13 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-104
- UPD: Directory structure.

* Mon Apr 08 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-103
- UPD: Requires.

* Sat Mar 30 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-102
- UPD: Directory structure.

* Sat Mar 30 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- UPD: Shell scripts.

* Wed Jan 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
