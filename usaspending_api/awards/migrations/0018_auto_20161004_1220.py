# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0017_auto_20160929_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='by_direct_reimbursable_fun',
            new_name='by_direct_reimbursable_funding_source',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='deobligations_recov_by_awa_cpe',
            new_name='deobligations_recoveries_refunds_of_prior_year_by_award_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='gross_outlay_amount_by_awa_cpe',
            new_name='gross_outlay_amount_by_award_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='gross_outlay_amount_by_awa_fyb',
            new_name='gross_outlay_amount_by_award_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='gross_outlays_delivered_or_cpe',
            new_name='gross_outlays_delivered_orders_paid_total_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='gross_outlays_delivered_or_fyb',
            new_name='gross_outlays_delivered_orders_paid_total_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='gross_outlays_undelivered_cpe',
            new_name='gross_outlays_undelivered_orders_prepaid_total_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='gross_outlays_undelivered_fyb',
            new_name='gross_outlays_undelivered_orders_prepaid_total_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='obligations_delivered_orde_cpe',
            new_name='obligations_delivered_orders_unpaid_total_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='obligations_delivered_orde_fyb',
            new_name='obligations_delivered_orders_unpaid_total_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='obligations_incurred_byawa_cpe',
            new_name='obligations_incurred_total_by_award_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='obligations_undelivered_or_cpe',
            new_name='obligations_undelivered_orders_unpaid_total_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='obligations_undelivered_or_fyb',
            new_name='obligations_undelivered_orders_unpaid_total_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl480100_undelivered_or_cpe',
            new_name='ussgl480100_undelivered_orders_obligations_unpaid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl480100_undelivered_or_fyb',
            new_name='ussgl480100_undelivered_orders_obligations_unpaid_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl480200_undelivered_or_cpe',
            new_name='ussgl480200_undelivered_orders_oblig_prepaid_advanced_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl480200_undelivered_or_fyb',
            new_name='ussgl480200_undelivered_orders_oblig_prepaid_advanced_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl483100_undelivered_or_cpe',
            new_name='ussgl483100_undelivered_orders_oblig_transferred_unpaid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl483200_undelivered_or_cpe',
            new_name='ussgl483200_undeliv_orders_oblig_transferred_prepaid_adv_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl487100_downward_adjus_cpe',
            new_name='ussgl487100_down_adj_pri_unpaid_undel_orders_oblig_recov_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl487200_downward_adjus_cpe',
            new_name='ussgl487200_down_adj_pri_ppaid_undel_orders_oblig_refund_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl488100_upward_adjustm_cpe',
            new_name='ussgl488100_upward_adjust_pri_undeliv_order_oblig_unpaid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl488200_upward_adjustm_cpe',
            new_name='ussgl488200_up_adjust_pri_undeliv_order_oblig_ppaid_adv_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl490100_delivered_orde_cpe',
            new_name='ussgl490100_delivered_orders_obligations_unpaid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl490100_delivered_orde_fyb',
            new_name='ussgl490100_delivered_orders_obligations_unpaid_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl490200_delivered_orde_cpe',
            new_name='ussgl490200_delivered_orders_obligations_paid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl490800_authority_outl_cpe',
            new_name='ussgl490800_authority_outlayed_not_yet_disbursed_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl490800_authority_outl_fyb',
            new_name='ussgl490800_authority_outlayed_not_yet_disbursed_fyb',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl493100_delivered_orde_cpe',
            new_name='ussgl493100_delivered_orders_oblig_transferred_unpaid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl497100_downward_adjus_cpe',
            new_name='ussgl497100_down_adj_pri_unpaid_deliv_orders_oblig_recov_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl497200_downward_adjus_cpe',
            new_name='ussgl497200_down_adj_pri_paid_deliv_orders_oblig_refund_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl498100_upward_adjustm_cpe',
            new_name='ussgl498100_upward_adjust_pri_deliv_orders_oblig_unpaid_cpe',
        ),
        migrations.RenameField(
            model_name='financialaccountsbyawards',
            old_name='ussgl498200_upward_adjustm_cpe',
            new_name='ussgl498200_upward_adjust_pri_deliv_orders_oblig_paid_cpe',
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='appropriation_account_balances',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.AppropriationAccountBalances'),
        ),
        migrations.AlterField(
            model_name='financialaccountsbyawards',
            name='object_class',
            field=models.ForeignKey(db_column='object_class', on_delete=django.db.models.deletion.DO_NOTHING, to='references.RefObjectClassCode'),
        ),
    ]
